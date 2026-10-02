# -*- coding: utf-8 -*-
"""Generates the four case-study detail pages.

The mirrored export only shipped the case-study index, so `/case-study/<slug>`
had nothing behind it. These pages reuse the index page's <head> verbatim - the
same webfonts, breakpoints and design tokens - and add a small stylesheet and a
vanilla reveal script, so they match the rest of the site without booting
Framer's runtime a second time.
"""

import os
import re

import content

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

STUDIES = [
    {
        "slug": "enterprise-graphrag",
        "title": "Enterprise GraphRAG Knowledge Assistant",
        "client": "Evernorth Health Services",
        "role": "Machine Learning Advisor",
        "timeline": "2024 - 2026",
        "stack": "Python, LangChain, LangGraph, knowledge graphs, LLM evaluation",
        "tags": ["GraphRAG", "RAG", "Knowledge Graphs", "Healthcare"],
        "accent": "#36c5f0",
        "lead": "A GraphRAG knowledge assistant for enterprise healthcare data, built so "
                "the answers could be traced back to a source instead of trusted on faith.",
        "sections": [
            ("The problem", [
                "Enterprise question answering over policy, procedure and benefit "
                "documentation fails in a specific and repeatable way. Vector search "
                "finds the passages that sound like the question, then the model "
                "answers from whatever it managed to retrieve. When the real answer "
                "depends on joining facts across documents - which policy version "
                "applies to this member, in this state, under this plan - the system "
                "either misses it or invents it.",
                "The team also had a governance constraint that ruled out the usual "
                "escape hatch. A confident wrong answer in this domain is worse than no "
                "answer, and every claim had to be attributable to a source a reviewer "
                "could open.",
            ]),
            ("The approach", [
                "I designed and prototyped a GraphRAG pipeline that treats structure "
                "as first-class. Ingestion normalises documents and extracts entities "
                "and relationships into a graph; retrieval runs conventional vector "
                "search first, then expands the top passages through graph traversal to "
                "pull in connected entities, their neighbours and their governing "
                "documents. The generator receives that expanded context together with "
                "the source identifiers.",
                "Alongside it I built a multi-agent layer with LangGraph. A router "
                "decides whether a question needs retrieval, a tool call, or a "
                "clarification; a retrieval agent runs the hybrid search and traversal; "
                "a generation agent writes the answer under a strict grounding "
                "contract. Every hop is checkpointed so a failed run resumes instead "
                "of restarting.",
                "Throughout, the graph was deliberately narrow. A small ontology over "
                "the entities the questions actually join proved far more useful than a "
                "broader one, because a stale graph produces confidently wrong answers "
                "that look identical to correct ones.",
            ]),
            ("What shipped", [
                "A working knowledge assistant with graph-enhanced retrieval, "
                "relationship-aware multi-hop context, and source attribution on every "
                "claim. Alongside it, an Excel reporting agent built with LangChain "
                "tools and guardrails cut roughly 60 percent of manual processing, and "
                "targeted contact-centre workflows were associated with a 25 percent "
                "improvement in first-response resolution.",
                "Evaluation came before polish: labelled question sets, retrieval "
                "metrics, groundedness scoring and LangSmith traces wired into the "
                "delivery loop so regressions surfaced before users did.",
            ]),
            ("What I would do differently", [
                "I would start with a smaller ontology and a larger evaluation set. The "
                "graph was the interesting part of the project, and it got more of my "
                "attention than the ground truth did, even though the ground truth is "
                "what told us whether any of it worked.",
            ]),
        ],
    },
    {
        "slug": "multi-agent-copilot",
        "title": "Multi-Agent RAG &amp; Copilot Platform",
        "client": "Evernorth Health Services",
        "role": "Machine Learning Advisor",
        "timeline": "2024 - 2026",
        "stack": "LangGraph, LangChain, FastAPI, AWS, OpenTelemetry",
        "tags": ["Agentic AI", "Multi-Agent", "Orchestration"],
        "accent": "#ecb22e",
        "lead": "A copilot that routes, retrieves and acts - built around explicit "
                "state, bounded retries and an honest stopping condition.",
        "sections": [
            ("The problem", [
                "The workflows we were asked to automate were not single-shot prompts. "
                "They branched: some questions needed a lookup, some needed a system "
                "call, some needed a human to approve an action before anything was "
                "written. Expressing that as one long prompt produced an agent that was "
                "clever in the demo and unpredictable in production.",
                "The practical symptoms were familiar: duplicated tool calls after a "
                "retry, state lost when a user closed the tab mid-task, and cost that "
                "spiked without anyone noticing until the invoice arrived.",
            ]),
            ("The approach", [
                "I modelled each workflow as an explicit state machine in LangGraph. "
                "Nodes do one thing, edges encode the routing decision, and a "
                "checkpoint is written after every meaningful step. That single change "
                "turned a fragile chain of prompts into something resumable and "
                "inspectable.",
                "Tools were designed to be narrow and typed. Read tools are freely "
                "retryable; anything with a side effect carries an idempotency key "
                "derived from the run and the step. Errors return a machine-readable "
                "code with a message written for the model, because a precise failure "
                "is recoverable and a stack trace is not.",
                "Cost and runaway behaviour were handled as safety limits rather than "
                "optimisations: token budgets per request, a hard ceiling on tool "
                "calls, and an explicit finish signal so the agent hands back what it "
                "has and describes what is still unknown.",
            ]),
            ("What shipped", [
                "Multi-agent RAG and copilot workflows running with routing, tool "
                "calling, stateful orchestration, guardrails and defined "
                "failure-handling behaviour, served through Python and FastAPI services "
                "deployed on AWS with S3, SQS, Lambda and SageMaker, containerised "
                "with CI/CD behind each release.",
                "LangSmith and Langfuse traces made the reasoning path visible in "
                "production, which is what let us tune routing without guessing.",
            ]),
            ("What I would do differently", [
                "I would have shipped single-agent versions first and split them only "
                "where routing genuinely required it. Multi-agent orchestration is a "
                "response to real branching, not a starting architecture, and every "
                "extra agent is another place for state to get lost.",
            ]),
        ],
    },
    {
        "slug": "expertgpt-excel-agent",
        "title": "ExpertGPT Excel Agent",
        "client": "Evernorth Health Services",
        "role": "Machine Learning Advisor",
        "timeline": "2025 - 2026",
        "stack": "LangChain, guardrails, Python, FastAPI",
        "tags": ["Automation", "Guardrails", "LLMOps"],
        "accent": "#2fbc81",
        "lead": "An agent that turned a recurring manual reporting task into a "
                "reviewed, auditable workflow.",
        "sections": [
            ("The problem", [
                "A recurring reporting task consumed hours of manual effort every week: "
                "pull figures, reshape them, write the commentary. It was the kind of "
                "work that does not fail loudly. It is slow, it is dull, and it is "
                "exactly the sort of thing that quietly absorbs a surprising amount of "
                "an experienced person's week.",
                "Automating it was not hard because of the model. It was hard because "
                "the task had to stay auditable, and because the output fed into "
                "reporting that other people signed off on.",
            ]),
            ("The approach", [
                "I wrapped the manual steps as explicit LangChain tools rather than "
                "letting the model improvise a workflow. Each tool has a narrow schema, "
                "a clear description of when it applies, and a structured error path. "
                "The agent's job became selection and sequencing, which is what models "
                "are genuinely good at.",
                "Guardrails sit at three levels. Inputs are validated and normalised "
                "before the model sees them; outputs are schema-constrained and "
                "re-validated with a specific complaint the agent can act on; and tool "
                "permissions are enforced in the tool layer, where the side effect "
                "actually happens, rather than in the prompt where they are only a "
                "suggestion.",
                "Because the output was reviewed, the agent reports what it did and "
                "where every number came from, so a reviewer could verify rather than "
                "trust.",
            ]),
            ("What shipped", [
                "An agentic reporting workflow that reduced manual processing and "
                "reporting effort by approximately 60 percent, with guardrails, "
                "structured outputs and an audit trail suitable for sign-off.",
            ]),
            ("What I would do differently", [
                "I would build the regression set before the guardrails rather than "
                "after. The guardrails were right, but they were tuned against anecdotes "
                "instead of a labelled set, and we spent a fortnight proving a case we "
                "should have caught in the first week.",
            ]),
        ],
    },
    {
        "slug": "llm-analysis-pipeline",
        "title": "Asynchronous LLM Analysis Pipeline",
        "client": "AWS",
        "role": "Senior AI/ML Associate",
        "timeline": "2026",
        "stack": "AWS SQS, Lambda, S3, Bedrock, SageMaker, Docker, CI/CD",
        "tags": ["AWS", "Serverless", "LLMOps"],
        "accent": "#19bd8c",
        "lead": "A reusable asynchronous pipeline for LLM analysis work, designed to be "
                "copied rather than admired.",
        "sections": [
            ("The problem", [
                "Analysis jobs have an awkward shape. They arrive in bursts, they are "
                "slow, they fail in ways that need isolating, and they are usually one "
                "of several jobs in a business rather than the business itself. Running "
                "them inside a request handler or a notebook scales badly and fails "
                "badly.",
                "The useful outcome was not one pipeline. It was a pattern that a team "
                "could adopt without redesigning it.",
            ]),
            ("The approach", [
                "The pipeline is deliberately boring. SQS receives the job, a router "
                "Lambda classifies and enriches it, prompts and context are staged in "
                "S3, an analysis Lambda calls the model and writes structured output "
                "back to S3, and a completion marker lets downstream consumers pick up "
                "results asynchronously.",
                "Each stage is isolated on purpose. A poison message fails one Lambda "
                "invocation instead of the batch, dead-letter queues capture what needs "
                "a human, and the staged context in S3 is what makes a run replayable "
                "after a model or prompt change.",
                "Serving the model is deliberately separate from the orchestration. "
                "Analysis can run against Bedrock or SageMaker without touching the "
                "queueing logic, which is the difference between a pattern and a "
                "one-off.",
            ]),
            ("What shipped", [
                "A production pipeline running on AWS with containerised deployment "
                "and CI/CD, documented and reused as the default shape for asynchronous "
                "LLM analysis work rather than a bespoke build per use case.",
            ]),
            ("What I would do differently", [
                "I would put the observability in the first commit. Traces per job, "
                "token counts per stage and a cost metric per completed analysis would "
                "have turned capacity planning from guesswork into arithmetic.",
            ]),
        ],
    },
]

CSS = """
:root{--ink:#111212;--paper:#fff;--muted:#767777;--line:#111212}
*{box-sizing:border-box;-webkit-font-smoothing:antialiased}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:"Inter Display","Inter","Inter Placeholder",sans-serif;}
a{color:inherit}
.cs{max-width:1100px;margin:0 auto;padding:0 24px}
.crumb{display:flex;gap:12px;align-items:center;padding:22px 0;font-size:13px;
  font-family:"DM Mono",monospace;text-transform:uppercase;letter-spacing:.06em}
.crumb a{text-decoration:none;border-bottom:1.5px solid var(--ink);padding-bottom:2px}
.hero{padding:48px 0 40px;border-bottom:2px solid var(--ink)}
.kicker{display:inline-block;background:var(--accent);border:2px solid var(--ink);
  padding:6px 12px;font-family:"DM Mono",monospace;font-size:12px;
  text-transform:uppercase;letter-spacing:.08em;transform:rotate(-2deg)}
h1{font-size:clamp(40px,7vw,84px);line-height:.98;letter-spacing:-.035em;
  margin:26px 0 18px;font-weight:700;max-width:16ch}
.lead{font-size:clamp(19px,2.4vw,26px);line-height:1.35;letter-spacing:-.015em;
  max-width:38ch;font-weight:500}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));
  gap:1px;background:var(--ink);border:2px solid var(--ink);margin:36px 0 0}
.meta div{background:var(--paper);padding:16px 18px}
.meta dt{font-family:"DM Mono",monospace;font-size:11px;text-transform:uppercase;
  letter-spacing:.1em;color:var(--muted);margin:0 0 6px}
.meta dd{margin:0;font-size:16px;font-weight:500;line-height:1.35}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:26px 0 0}
.chip{border:2px solid var(--ink);padding:6px 12px;font-size:13px;font-weight:500}
section{padding:52px 0;border-bottom:2px solid var(--ink)}
section h2{font-size:clamp(26px,3.4vw,40px);letter-spacing:-.03em;margin:0 0 20px;
  font-weight:700}
section p{font-size:18px;line-height:1.6;max-width:66ch;margin:0 0 18px;color:#232525}
.reveal{opacity:0;transform:translateY(26px);
  transition:opacity .7s cubic-bezier(.2,.7,.2,1),transform .7s cubic-bezier(.2,.7,.2,1)}
.reveal.in{opacity:1;transform:none}
.pager{display:flex;justify-content:space-between;gap:20px;padding:44px 0 70px;
  font-size:20px;font-weight:600}
.pager a{text-decoration:none;border-bottom:2px solid var(--ink)}
.pager span{font-family:"DM Mono",monospace;font-size:12px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--muted);display:block;margin-bottom:6px}
footer{border-top:2px solid var(--ink);padding:30px 0 60px;font-size:14px;
  font-family:"DM Mono",monospace;letter-spacing:.04em}
@media (prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}
"""

SCRIPT = """
<script>
(function(){
  var items=document.querySelectorAll('.reveal');
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!('IntersectionObserver' in window)||reduce){
    Array.prototype.forEach.call(items,function(el){el.classList.add('in')});
    return;
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){entry.target.classList.add('in');io.unobserve(entry.target)}
    });
  },{threshold:.12,rootMargin:'0px 0px -8% 0px'});
  Array.prototype.forEach.call(items,function(el){io.observe(el)});
})();
</script>
"""


def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def head_from_index(index_html, study):
    head = index_html[:index_html.find("</head>") + 7]
    head = re.sub(r'\s*<script\b[^>]*>\s*</script>', "", head)
    head = re.sub(r'\s*<script\b[^>]*>', "", head)
    head = re.sub(r'\s*</script>', "", head)

    title = "%s \u2014 %s" % (study["title"], content.NAME)
    head = head.replace(
        "<title>%s</title>" % content.PAGE_TITLES["case-study.html"],
        "<title>%s</title>" % esc(title))
    head = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="%s">' % esc(study["lead"]), head, count=1)
    head = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        '<meta property="og:title" content="%s">' % esc(title), head, count=1)
    head = re.sub(
        r'<meta name="twitter:title" content="[^"]*">',
        '<meta name="twitter:title" content="%s">' % esc(title), head, count=1)
    head = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        '<meta property="og:description" content="%s">' % esc(study["lead"]),
        head, count=1)
    head = re.sub(
        r'<meta name="twitter:description" content="[^"]*">',
        '<meta name="twitter:description" content="%s">' % esc(study["lead"]),
        head, count=1)
    return head


def render(index_html, study, prev_slug, prev_title, next_slug, next_title):
    meta = [("Client", study["client"]), ("Role", study["role"]),
            ("Timeline", study["timeline"]), ("Stack", study["stack"])]

    body = ['<main class="cs">']
    body.append(
        '<nav class="crumb"><a href="/">Home</a>'
        '<span aria-hidden="true">&rsaquo;</span>'
        '<a href="/case-study">Case Studies</a></nav>'
    )
    body.append('<header class="hero">')
    body.append('<span class="kicker">Case study</span>')
    body.append("<h1>%s</h1>" % esc(study["title"]))
    body.append('<p class="lead">%s</p>' % esc(study["lead"]))
    body.append('<dl class="meta">')
    for label, value in meta:
        body.append("<div><dt>%s</dt><dd>%s</dd></div>" % (label, esc(value)))
    body.append("</dl>")
    body.append('<div class="chips">')
    for tag in study["tags"]:
        body.append('<span class="chip">%s</span>' % esc(tag))
    body.append("</div>")
    body.append("</header>")

    for heading, paragraphs in study["sections"]:
        body.append('<section class="reveal"><h2>%s</h2>' % esc(heading))
        for text in paragraphs:
            body.append("<p>%s</p>" % esc(text))
        body.append("</section>")

    body.append('<nav class="pager">')
    if prev_slug:
        body.append('<a href="/case-study/%s"><span>Previous</span>%s</a>'
                    % (prev_slug, esc(prev_title)))
    else:
        body.append("<span></span>")
    if next_slug:
        body.append('<a href="/case-study/%s" style="text-align:right"><span>Next</span>%s</a>'
                    % (next_slug, esc(next_title)))
    body.append("</nav>")
    body.append("</main>")

    body.append(
        '<footer class="cs">%s \u2014 Senior AI Engineer \u00b7 Hyderabad, India '
        '\u00b7 <a href="/contact">Contact</a></footer>' % content.NAME
    )

    head = head_from_index(index_html, study)
    return (
        head
        + "<body>"
        + "".join(body)
        + "<style>%s</style>" % CSS
        + SCRIPT
        + "</body></html>"
    )


def build():
    index_html = open(os.path.join(ROOT, "case-study.html"), encoding="utf-8").read()
    out_dir = os.path.join(ROOT, "case-study")
    os.makedirs(out_dir, exist_ok=True)

    written = []
    count = len(STUDIES)
    for i, study in enumerate(STUDIES):
        prev_slug = STUDIES[i - 1]["slug"] if i else None
        prev_title = STUDIES[i - 1]["title"] if i else None
        nxt = STUDIES[(i + 1) % count]
        html = render(index_html, study, prev_slug, prev_title,
                      nxt["slug"], nxt["title"])
        out = os.path.join(out_dir, study["slug"] + ".html")
        with open(out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(html)
        written.append("case-study/%s.html" % study["slug"])

    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8",
              newline="\n") as fh:
        fh.write(not_found(index_html))
    written.append("404.html")
    return written


NOT_FOUND = {
    "slug": "404",
    "title": "Page not found",
    "client": content.NAME,
    "role": "Senior AI Engineer",
    "timeline": content.LOCATION,
    "stack": "Agentic AI, GraphRAG, LLMOps",
    "tags": [],
    "accent": "#e01e5a",
    "lead": "That route does not resolve. Everything on this site does though.",
    "sections": [
        ("Try one of these", []),
    ],
}

LINKS = [
    ("Home", "/"),
    ("About", "/about"),
    ("Case Studies", "/case-study"),
    ("Services", "/services"),
    ("Blog", "/blog"),
    ("Contact", "/contact"),
]


def not_found(index_html):
    body = ['<main class="cs">']
    body.append('<header class="hero">')
    body.append('<span class="kicker">Error 404</span>')
    body.append("<h1>Page not found</h1>")
    body.append('<p class="lead">That route does not resolve. Everything on this '
                'site does though.</p>')
    body.append('<div class="chips">')
    for label, href in LINKS:
        body.append('<a class="chip" href="%s">%s</a>' % (href, label))
    body.append("</div>")
    body.append("</header></main>")
    body.append('<footer class="cs">%s &middot; <a href="/">Home</a></footer>'
                % content.NAME)

    head = head_from_index(index_html, NOT_FOUND)
    return (head + "<body>" + "".join(body) + "<style>%s</style>" % CSS
            + "</body></html>")


if __name__ == "__main__":
    for path in build():
        print("page  ", path)