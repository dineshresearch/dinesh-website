/**
 * Zero-dependency static server for the exported Framer site.
 *
 *   npm start            -> http://localhost:5173
 *   PORT=8080 npm start
 *
 * The site uses clean URLs (/about, /blog/evaluation-is-the-product) while the
 * files on disk are plain .html files, so this resolves both. Query strings on
 * asset URLs (?width=1200) are ignored, matching how the CDN URLs behaved.
 */

import { createServer } from "node:http";
import { createReadStream, statSync } from "node:fs";
import { extname, join, normalize, sep } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = process.env.ROOT_DIR
  ? process.env.ROOT_DIR.replace(/[\\/]+$/, "")
  : fileURLToPath(new URL(".", import.meta.url));
const PORT = Number(process.env.PORT) || 5173;
const HOST = process.env.HOST || "127.0.0.1";

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".map": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".avif": "image/avif",
  ".gif": "image/gif",
  ".ico": "image/x-icon",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
  ".ttf": "font/ttf",
  ".txt": "text/plain; charset=utf-8",
  ".xml": "application/xml; charset=utf-8",
  ".pdf": "application/pdf",
  ".framercms": "application/octet-stream",
};

/** Everything under here is a build artifact, never served. */
const PRIVATE = new Set(["_original-export", "tools", "node_modules"]);

function resolve(urlPath) {
  const clean = normalize(decodeURIComponent(urlPath.split("?")[0].split("#")[0]))
    .replace(/^(\.\.[/\\])+/, "")
    .replace(/^[/\\]+/, "");
  if (clean === "" || clean === ".") return "index.html";

  const base = join(ROOT, clean);
  if (!base.startsWith(ROOT.endsWith(sep) ? ROOT : ROOT + sep)) return null;
  if (PRIVATE.has(clean.split(/[/\\]/)[0])) return null;

  const candidates = [
    clean,
    clean + ".html",
    join(clean, "index.html"),
  ];
  for (const rel of candidates) {
    const file = join(ROOT, rel);
    if (!file.startsWith(ROOT.endsWith(sep) ? ROOT : ROOT + sep)) continue;
    try {
      if (statSync(file).isFile()) return file;
    } catch {
      /* keep looking */
    }
  }
  return null;
}

/**
 * Framer's CMS loader fetches its .framercms blobs as byte slices, asking for
 * "?range=start-end". It then does `new Uint8Array(declaredLength)` and copies
 * the response in, so the server has to return exactly the requested window or
 * the router dies on every client-side navigation.
 */
function rangeOf(url, size) {
  const match = /[?&]range=(\d+)-(\d+)/.exec(url || "");
  if (!match) return null;
  const start = Number(match[1]);
  const end = Math.min(Number(match[2]), size - 1);
  if (start >= size || start > end) return null;
  return { start, end };
}

const server = createServer((req, res) => {
  const file = resolve(req.url || "/");

  if (!file) {
    const notFound = join(ROOT, "404.html");
    res.writeHead(404, { "content-type": MIME[".html"] });
    try {
      createReadStream(notFound).pipe(res);
    } catch {
      res.end("<h1>404</h1><p><a href=\"/\">Home</a></p>");
    }
    return;
  }

  const type = MIME[extname(file).toLowerCase()] || "application/octet-stream";
  let size;
  try {
    size = statSync(file).size;
  } catch {
    res.writeHead(500).end("Internal error");
    return;
  }

  const range = rangeOf(req.url, size);
  if (range) {
    res.writeHead(206, {
      "content-type": type,
      "content-length": range.end - range.start + 1,
      "content-range": `bytes ${range.start}-${range.end}/${size}`,
      "accept-ranges": "bytes",
      "cache-control": "no-cache",
    });
    if (req.method === "HEAD") return res.end();
    return createReadStream(file, { start: range.start, end: range.end }).pipe(res);
  }

  res.writeHead(200, {
    "content-type": type,
    "content-length": size,
    "accept-ranges": "bytes",
    "cache-control": "no-cache",
  });
  if (req.method === "HEAD") return res.end();
  createReadStream(file).pipe(res);
});

server.listen(PORT, HOST, () => {
  console.log("  Amara Dinesh Kumar — Senior AI Engineer");
  console.log(`  http://${HOST}:${PORT}\n`);
  console.log("  Press Ctrl+C to stop.");
});