# Amara Dinesh Kumar — Senior AI Engineer (portfolio site)

A static portfolio site built from the Nudge-Folio Framer template, personalised
for Amara Dinesh Kumar's resume (Agentic AI, GraphRAG, RAG, LLMOps, AWS).

## Layout

- `index.html`, `about.html`, `services.html`, `case-study.html`, `contact.html`,
  `404.html` — top-level pages
- `blog/index.html` + one `.html` per post (the section is labelled Blog)
- `case-study/<slug>.html` — one per project
- `js/`, `images/` — static assets (Framer runtime, fonts, images)
- `tools/` — build + check scripts
- `_original-export/` — pristine copy of the downloaded template

## Run locally

```powershell
node server.mjs          # http://localhost:5173
```

Or with npm:

```powershell
npm start
```

## Rebuild from the template

```powershell
python tools\build.py
```

This regenerates the `.html` pages, rewrites `js/` bundles with the new copy
(`tools/content.py`), injects the site chrome (résumé button, contact links,
hidden Framer badge mount point), and rebuilds the site-search index
(`tools/searchindex.py`).

## Verify

```powershell
node tools\check-links.mjs      # every local link/src resolves to a real file
node tools\browser-check.mjs    # headless-Chrome pass over every route
```

## Notes

- Client rendering: the export's SSR split-text markup does not match what the
  bundled split-text component renders, so `tools/content.py` patches
  `js/react.73opg4pm.mjs` to mount with `createRoot(...).render(...)`. Every
  route now loads with no console errors.
- Framer's "Made with Framer" badge and "Buy this template" button are hidden
  with CSS rather than removed: the runtime still mounts both into
  `#__framer-badge-container`, and removing that mount point makes React throw.
- The résumé button (`[data-site-resume]`) and the contact link row
  (`[data-site-contact]`) live after `</body>`'s badge container because the
  runtime rewrites `<head>` on every route and would drop injected markup there.
- `/play-ground` was removed from the build, the search index and the nav. The
  SSR nav anchor is stripped in `tools/content.py`; the client-rendered copy is
  hidden by CSS.
- Four case-study detail pages are generated outside Framer's router. A capture
  -phase click interceptor in `js/rerouter.js` (`STATIC_NAV`) forces a full page
  load for them instead of letting the SPA router fail.
- Contact details live in `CONTACT` in `tools/content.py`. Note the ordering
  constraint on the global replacements: the template's bare `linkedin.com` and
  `github.com` links must be rewritten before the Facebook/Instagram pairs emit
  the real profile URLs, otherwise they get matched a second time.
