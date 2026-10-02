"""Rebuild the static site from the pristine Framer export in _original-export/.

The upstream mirror stored every page as an extension-less file ("about",
"blog/index") with document-relative asset URLs, which only resolved when every
page happened to sit at the exact same path depth as the live Framer site.
This script rewrites those paths to be root-absolute so any static server can
serve the site from a domain root, then applies the copy in tools/content.py.

Usage:  python tools/build.py
"""

import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_original-export")

# (source file, output file, depth, sibling_links)
# sibling_links: the page links to its peers inside the same folder (/blog/).
PAGES = [
    ("index", "index.html", 0, False),
    ("about", "about.html", 0, False),
    ("services", "services.html", 0, False),
    ("case-study", "case-study.html", 0, False),
    ("contact", "contact.html", 0, False),
    ("blog/index", "blog/index.html", 1, False),
]


def journal_pages():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import content

    return [(os.path.join("blog", src), "blog/%s.html" % new, 1, True)
            for new, (src, _t, _c, _s) in content.POSTS.items()]


PAGES.extend(journal_pages())

# Asset references: "images/x.png" / "../images/x.png" / "js/x.mjs" -> "/images/x.png"
ASSET_RE = re.compile(r'''(?<=["'(,])(?:\.{1,2}/+)?(images|js)/''')


def absolutise(html, depth, sibling=False):
    html = html.replace('<base href="">', '<base href="/">')
    html = html.replace('<base href="../">', '<base href="/">')

    # Journal posts link to each other with "./slug", which means /blog/slug.
    if sibling:
        html = re.sub(r'''href="\./([^"/#?]+)"''', r'href="/blog/\1"', html)

    html = re.sub(r'''href="\.{1,2}/''', 'href="/', html)
    html = ASSET_RE.sub(r'/\1/', html)
    return html


def add_badge_container(html):
    """Framer's runtime mounts its badge and "Buy" button into one container.

    The export ships the CSS rule for it but never the element, so the runtime
    calls hydrateRoot(null, ...) and React throws on every page load. The same
    container carries the résumé download link, which is appended after it
    because the runtime rewrites <head> on every route and would drop markup
    injected there.
    """
    if content.BADGE_CONTAINER in html:
        return html
    return html.replace("</body>", content.RESUME_BANNER + "\n</body>", 1)


def personalise(html, dst):
    """Per-page fixes applied after the shared copy pass."""
    html = content.drop_inline_portrait(html)
    html = content.drop_playground_link(html)
    if dst == "contact.html":
        html = content.fix_contact_socials(html, is_bundle=False)
        html = html.replace("</body>", content.CONTACT_LINKS + "\n</body>", 1)
    html = content.hide_template_chrome(html)
    return html


def inject_chrome_css(html):
    if "data-site-chrome" in html:
        return html
    if "</head>" not in html:
        return html
    return html.replace("</head>", content.CHROME_CSS + "</head>", 1)


def finish(html, dst):
    html = personalise(html, dst)
    html = add_badge_container(html)
    return inject_chrome_css(html)


def build_pages():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import content

    written = []
    for src, dst, depth, sibling in PAGES:
        with open(os.path.join(SRC, src), encoding="utf-8") as fh:
            html = fh.read()
        html = absolutise(html, depth, sibling)
        html = content.apply(dst, html)
        html = finish(html, dst)
        out = os.path.join(ROOT, dst)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(html)
        written.append(dst)
    return written


def build_js():
    """Restore js/ from the pristine copy, then apply copy replacements."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import content

    src_js = os.path.join(SRC, "js")
    dst_js = os.path.join(ROOT, "js")
    for name in sorted(os.listdir(src_js)):
        with open(os.path.join(src_js, name), "rb") as fh:
            data = fh.read()
        path = "js/" + name
        blob = content.apply_bytes(path, data)
        page = content.MODULE_TO_PAGE.get(path)
        if page == "contact.html":
            blob = content.fix_contact_socials(
                blob.decode("utf-8"), is_bundle=True).encode("utf-8")
        elif b"m2ikrrxfhsxjyxqcmhtrp56ia.png?width=382" in blob:
            blob = content.drop_inline_portrait(
                blob.decode("utf-8")).encode("utf-8")
        with open(os.path.join(dst_js, name), "wb") as fh:
            fh.write(blob)


if __name__ == "__main__":
    stale = [p for p in ("index", "about", "services", "case-study", "contact",
                         "play-ground")
             if os.path.isfile(os.path.join(ROOT, p))]
    for name in stale:
        os.remove(os.path.join(ROOT, name))
    if stale:
        print("removed extension-less export files:", ", ".join(stale))

    written = build_pages()
    stale_pg = os.path.join(ROOT, "play-ground.html")
    if os.path.isfile(stale_pg):
        os.remove(stale_pg)
        print("stale  play-ground.html")
    for page in written:
        print("page  ", page)

    keep = {os.path.normcase(os.path.join(ROOT, p)) for p in written}
    blog = os.path.join(ROOT, "blog")
    for name in os.listdir(blog):
        full = os.path.join(blog, name)
        if name.endswith(".html") and os.path.normcase(full) not in keep:
            os.remove(full)
            print("stale ", "blog/" + name)

    build_js()
    print("js/   refreshed")

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import case_studies
    for page in case_studies.build():
        print("page  ", page)

    for name in sorted(os.listdir(os.path.join(ROOT, "case-study"))):
        path = os.path.join(ROOT, "case-study", name)
        with io.open(path, encoding="utf-8") as fh:
            html = fh.read()
        with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(finish(html, "case-study/" + name))

    import searchindex
    print("search index:", searchindex.build(), "routes")