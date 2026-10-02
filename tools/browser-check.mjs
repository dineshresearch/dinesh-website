/**
 * Loads every page in headless Chrome and reports console errors, uncaught
 * exceptions and failed network requests.
 *
 *   node tools/browser-check.mjs [baseUrl]
 *
 * Screenshots land in tools/screenshots/.
 */

import { spawn } from "node:child_process";
import { mkdirSync, existsSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { tmpdir } from "node:os";

const BASE = process.argv[2] || "http://127.0.0.1:5173";
const HERE = fileURLToPath(new URL(".", import.meta.url));
const SHOTS = join(HERE, "screenshots");
const PORT = 9333;

const CHROME = [
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
].find((p) => existsSync(p));

const ALL_ROUTES = [
  "/",
  "/about",
  "/services",
  "/case-study",
  "/case-study/enterprise-graphrag",
  "/case-study/multi-agent-copilot",
  "/case-study/expertgpt-excel-agent",
  "/case-study/llm-analysis-pipeline",
  "/contact",
  "/blog",
  "/blog/why-graphs-beat-flat-search",
  "/blog/shipping-agents-to-production",
  "/blog/tool-calling-without-the-chaos",
  "/blog/designing-agent-workflows-that-recover",
  "/blog/guardrails-that-actually-hold",
  "/blog/memory-state-and-checkpoints",
  "/blog/grounding-provenance-and-trust",
  "/blog/evaluation-is-the-product",
];

const ROUTES = process.env.ONLY
  ? process.env.ONLY.split(",")
  : ALL_ROUTES;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function waitForCdp() {
  for (let i = 0; i < 60; i += 1) {
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/json/version`);
      if (res.ok) return await res.json();
    } catch {
      /* not up yet */
    }
    await sleep(250);
  }
  throw new Error("Chrome DevTools endpoint never came up");
}

class Session {
  constructor(ws) {
    this.ws = ws;
    this.id = 0;
    this.pending = new Map();
    this.events = [];
    ws.addEventListener("message", (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        msg.error ? reject(new Error(JSON.stringify(msg.error))) : resolve(msg.result);
      } else if (msg.method) {
        this.events.push(msg);
      }
    });
  }

  send(method, params = {}) {
    this.id += 1;
    const id = this.id;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
      setTimeout(() => {
        if (this.pending.has(id)) {
          this.pending.delete(id);
          reject(new Error(method + " timed out"));
        }
      }, 30000);
    });
  }
}

function connect(url) {
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(url);
    ws.addEventListener("open", () => resolve(new Session(ws)));
    ws.addEventListener("error", (e) => reject(new Error("ws error " + e.message)));
  });
}

async function openTab(url) {
  const res = await fetch(
    `http://127.0.0.1:${PORT}/json/new?${encodeURIComponent(url)}`,
    { method: "PUT" },
  );
  return res.json();
}

async function check(route) {
  const target = await openTab("about:blank");
  const s = await connect(target.webSocketDebuggerUrl);

  await s.send("Runtime.enable");
  await s.send("Log.enable");
  await s.send("Network.enable");
  await s.send("Network.setCacheDisabled", { cacheDisabled: true });
  await s.send("Page.enable");

  await s.send("Page.navigate", { url: BASE + route });
  await sleep(Number(process.env.SETTLE || 8000));

  const problems = [];
  for (const ev of s.events) {
    if (ev.method === "Runtime.exceptionThrown") {
      const d = ev.params.exceptionDetails;
      problems.push(`exception: ${d.text} ${d.exception?.description || ""}`.trim());
    }
    if (ev.method === "Log.entryAdded" && ev.params.entry.level === "error") {
      problems.push(`console: ${ev.params.entry.text}`);
    }
    if (ev.method === "Network.loadingFailed" && !ev.params.canceled) {
      problems.push(`request failed: ${ev.params.errorText} ${ev.params.type}`);
    }
    if (ev.method === "Network.responseReceived") {
      const { status, url } = ev.params.response;
      if (status >= 400) problems.push(`http ${status}: ${url}`);
    }
  }

  const shot = await s.send("Page.captureScreenshot", { format: "png" });
  writeFileSync(join(SHOTS, route.replace(/[/?]/g, "_") + ".png"),
                Buffer.from(shot.data, "base64"));

  await fetch(`http://127.0.0.1:${PORT}/json/close/${target.id}`);
  s.ws.close();
  return [...new Set(problems)];
}

async function main() {
  if (!CHROME) throw new Error("no Chrome or Edge found");
  mkdirSync(SHOTS, { recursive: true });
  const profile = join(tmpdir(), "site-check-profile");
  const chrome = spawn(CHROME, [
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-first-run",
    "--disable-extensions",
    "--hide-scrollbars",
    "--window-size=1440,1000",
    `--user-data-dir=${profile}`,
    `--remote-debugging-port=${PORT}`,
    "about:blank",
  ], { stdio: "ignore" });

  let failures = 0;
  try {
    await waitForCdp();
    for (const route of ROUTES) {
      const problems = await check(route);
      if (problems.length) {
        failures += 1;
        console.log(`\nFAIL ${route}`);
        for (const p of problems.slice(0, 12)) console.log("      " + p);
      } else {
        console.log(`ok   ${route}`);
      }
    }
  } finally {
    chrome.kill();
  }
  console.log(failures ? `\n${failures} page(s) with problems` : "\nAll pages clean.");
  process.exit(failures ? 1 : 0);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});