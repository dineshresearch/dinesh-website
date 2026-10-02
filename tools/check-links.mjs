/**
 * Verifies the generated site: every local URL referenced from a page must
 * resolve to a real file, and no placeholder copy from the original template
 * may be left behind.
 *
 *   npm run check
 */

import { readdirSync, readFileSync, statSync } from "node:fs";
import { extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const PRIVATE = new Set(["_original-export", "tools", "node_modules"]);

const LEFTOVERS = [
  "Bejaman",
  "Nudge",
  "Meridian Health",
  "StyleBook",
  "Homestead",
  "North Light",
  "Northlight Consulting",
  "Meridian",
  "product designer",
  "Product Designer",
  "Framer Site",
  "salon",
  "therapist",
  "homebuyer",
];

function htmlFiles(dir = ROOT, acc = []) {
  for (const entry of readdirSync(dir)) {
    if (PRIVATE.has(entry)) continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) htmlFiles(full, acc);
    else if (entry.endsWith(".html")) acc.push(full);
  }
  return acc;
}

function exists(urlPath) {
  const clean = normalize(decodeURIComponent(urlPath.split("?")[0].split("#")[0]))
    .replace(/^(\.\.[/\\])+/, "")
    .replace(/^[/\\]+/, "");
  for (const rel of [clean, clean + ".html", join(clean, "index.html")]) {
    if (!rel) continue;
    try {
      if (statSync(join(ROOT, rel)).isFile()) return true;
    } catch {
      /* keep looking */
    }
  }
  return false;
}

function localRefs(html) {
  const refs = new Set();
  const attr = /(?:href|src|poster|data-framer-search-index|data-framer-search-index-fallback)="([^"]+)"/g;
  const srcset = /srcset="([^"]+)"/g;
  const cssUrl = /url\((['"]?)([^)'"]+)\1\)/g;
  const meta = /(?:content|property)="((?:images|js)\/[^"]+)"/g;
  for (const re of [attr, meta]) {
    for (const m of html.matchAll(re)) refs.add(m[1]);
  }
  for (const m of html.matchAll(srcset)) {
    for (const part of m[1].split(",")) refs.add(part.trim().split(/\s+/)[0]);
  }
  for (const m of html.matchAll(cssUrl)) {
    if (!/^(https?:|data:|#|\/)/.test(m[2])) refs.add(m[2]);
  }
  return [...refs].filter(
    (u) => u && !/^(https?:|data:|mailto:|tel:|#|\/\/)/.test(u),
  );
}

let broken = 0;
const leftovers = new Map();

for (const file of htmlFiles()) {
  const rel = file.slice(ROOT.length).replace(/\\/g, "/");
  const html = readFileSync(file, "utf8");

  for (const ref of localRefs(html)) {
    const target = ref.startsWith("/") ? ref : "/" + normalize(join("/" + rel.slice(0, rel.lastIndexOf("/") + 1), ref));
    if (!exists(target)) {
      console.log(`BROKEN  ${rel}\n          -> ${ref}`);
      broken += 1;
    }
  }

  for (const needle of LEFTOVERS) {
    const hits = html.split(needle).length - 1;
    if (hits) {
      if (!leftovers.has(needle)) leftovers.set(needle, []);
      leftovers.get(needle).push(`${rel} (${hits})`);
    }
  }
}

if (leftovers.size) {
  console.log("\nTemplate copy still present:");
  for (const [needle, where] of leftovers) {
    console.log(`  "${needle}" -> ${where.join(", ")}`);
  }
}

console.log(
  broken === 0
    ? "\nAll local links resolve."
    : `\n${broken} broken reference(s).`,
);

const CMS_BLOBS = [
  "js/hu3yniggg-chunk-default-0.framercms",
  "js/hu3yniggg-indexes-default-0.framercms",
  "js/d8jd2hbse-chunk-default-0.framercms",
  "js/d8jd2hbse-indexes-default-0.framercms",
];

let cmsMismatch = 0;
for (const rel of CMS_BLOBS) {
  const src = join(ROOT, "_original-export", rel);
  const out = join(ROOT, rel);
  const a = readFileSync(src);
  const b = readFileSync(out);
  if (!a.equals(b)) {
    console.log(`CMS blob was rewritten: ${rel} (${b.length} vs ${a.length} bytes)`);
    console.log("  The page bundles address these by hardcoded byte offsets, so this");
    console.log("  breaks CMS reads on every client-side navigation.");
    cmsMismatch += 1;
  }
}

process.exit(broken === 0 && leftovers.size === 0 && cmsMismatch === 0 ? 0 : 1);
