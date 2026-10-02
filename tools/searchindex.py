# -*- coding: utf-8 -*-
"""Regenerates Framer's site-search index from the pages we just wrote.

The mirrored index is a flat snapshot of the original template's copy. Left
alone it would keep answering searches with "therapists", "salons" and
"homebuyers", so it is rebuilt here from the real HTML in the same shape the
Framer runtime expects: {"<route>": {version, title, description, keywords,
h1..h6, p, codeblock, url}}.
"""

import html as htmllib
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

ROUTES = [
    ("/", "index.html"),
    ("/about", "about.html"),
    ("/services", "services.html"),
    ("/case-study", "case-study.html"),
    ("/contact", "contact.html"),
    ("/blog", "blog/index.html"),
]

TAGS = re.compile(r"<(h[1-6]|p)\b([^>]*)>(.*?)</\1>", re.S | re.I)
DROP = re.compile(r"<[^>]+>")


WORD_GAP = "␟"


def clean(fragment):
    """Flatten markup, then rejoin Framer's one-character-per-span headings."""
    fragment = re.sub(r"</span>\s*<span style=\"white-space:nowrap\">",
                      WORD_GAP, fragment)
    text = htmllib.unescape(DROP.sub(" ", fragment))
    text = re.sub(r"\s+", " ", text).replace("\u200e", "").strip()

    words = []
    for chunk in text.split(WORD_GAP):
        tokens = [t for t in chunk.split(" ") if t]
        if len(tokens) > 1 and all(len(t) == 1 for t in tokens):
            words.append("".join(tokens))
        else:
            words.append(chunk.strip())
    return " ".join(w for w in words if w)


def entry(route, filename, blog_posts):
    raw = open(os.path.join(ROOT, filename), encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", raw, re.S)
    desc = re.search(r'<meta name="description" content="([^"]*)"', raw)

    heads = {n: [] for n in range(1, 7)}
    paras = []
    for tag, attrs, inner in TAGS.findall(raw):
        text = clean(inner)
        if not text or len(text) > 400:
            continue
        level = int(tag[1]) if len(tag) > 1 and tag[1].isdigit() else 0
        bucket = heads[level] if level else paras
        if text not in bucket:
            bucket.append(text)

    # The Playground nav item is still in the DOM (hidden with CSS), so drop it
    # from search results along with the other chrome labels.
    skip = ("Home", "About", "Case Studies", "Services", "Blog",
            "Playground", "Contact", "Menu", "AD", "AK")
    if route == "/blog":
        heads[1] = ["blog"]
        paras = [t for t in paras if t not in skip]
    else:
        paras = [t for t in paras if t not in skip + ("Comment",)]

    return {
        "version": 1,
        "title": htmllib.unescape(title.group(1)) if title else route,
        "description": htmllib.unescape(desc.group(1)) if desc else "",
        "keywords": "",
        "h1": heads[1], "h2": heads[2], "h3": heads[3],
        "h4": heads[4], "h5": heads[5], "h6": heads[6],
        "p": paras,
        "codeblock": [],
        "url": route,
    }


def build():
    import case_studies
    import content

    posts = {slug: "blog/%s.html" % slug for slug in content.POSTS}

    routes = list(ROUTES)
    routes += [("/case-study/%s" % s["slug"], "case-study/%s.html" % s["slug"])
               for s in case_studies.STUDIES]
    routes += [("/blog/%s" % slug, path) for slug, path in posts.items()]

    index = {route: entry(route, path, posts) for route, path in routes}

    blob = json.dumps(index, ensure_ascii=False, separators=(",", ":"))
    for name in ("searchindex-bb4z3cltjmo6.json", "searchindex-x7crccyoa2nf.json"):
        with open(os.path.join(ROOT, "js", name), "w", encoding="utf-8",
                  newline="\n") as fh:
            fh.write(blob)
    return len(index)


if __name__ == "__main__":
    print("search index rebuilt with %d routes" % build())