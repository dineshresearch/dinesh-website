# -*- coding: utf-8 -*-
"""Every piece of copy on the site, derived from Amara Dinesh Kumar's resume.

`tools/build.py` replays the pristine Framer export in `_original-export/`
through the substitutions below to produce the final `.html` pages and a
patched `js/` bundle.

Nothing here may contain an ASCII double quote or a backslash: the same strings
are written into JavaScript template literals, JSON payloads and length-prefixed
`.framercms` blobs, and escaping them differently in each place is how these
files get corrupted.
"""

import json
import os
import re

NAME = "Amara Dinesh Kumar"
ROLE = "Senior AI Engineer"
LOCATION = "Hyderabad, India"
HERE = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT = os.path.join(os.path.dirname(HERE), "_original-export")

CONTACT = {
    "email": "mailto:email-dineshkumar.amara@gmail.com",
    "phone": "tel:+919629956726",
    "linkedin": "https://www.linkedin.com/in/amara-dinesh-kumar-7b141252",
    "github": "https://github.com/dineshresearch",
    "scholar": (
        "https://scholar.google.co.in/citations?user=ifPShVAAAAAJ&hl=en"
    ),
}
PHONE_DISPLAY = "+91 96299 56726"
EMAIL_DISPLAY = "email-dineshkumar.amara@gmail.com"

SITE_DESCRIPTION = (
    "Amara Dinesh Kumar is a Senior AI Engineer in Hyderabad, India with 12+ years "
    "in technology and 8+ in AI/ML, building production agentic AI, multi-agent "
    "orchestration, GraphRAG, knowledge graphs, RAG and LLM evaluation systems on AWS."
)

HOME_TITLE = NAME + " \u2014 Senior AI Engineer"

PAGE_TITLES = {
    "index.html": NAME + " \u2014 Senior AI Engineer | Agentic AI, GraphRAG and LLMOps",
    "about.html": "About \u2014 " + NAME + ", Senior AI Engineer",
    "services.html": "AI Engineering Services \u2014 " + NAME,
    "case-study.html": "Case Studies \u2014 " + NAME,
    "contact.html": "Contact \u2014 " + NAME,
    "blog/index.html": "Blog \u2014 " + NAME,
}

# ------------------------------------------------------------------- journal
# new slug -> (old export file, title, category, summary)
POSTS = {
    "why-graphs-beat-flat-search": (
        "ideas-need-silence",
        "Why Graphs Beat Flat Search",
        "RAG & Retrieval",
        "Vector search finds passages. A knowledge graph finds relationships. Where "
        "GraphRAG genuinely beats conventional RAG, and where it still does not.",
    ),
    "shipping-agents-to-production": (
        "beyond-the-screen",
        "Shipping Agents to Production",
        "Agentic AI",
        "What actually breaks when a multi-agent system leaves the notebook: retries, "
        "state, cost ceilings, evaluation and the human approval path.",
    ),
    "tool-calling-without-the-chaos": (
        "everyday-beauty",
        "Tool Calling Without the Chaos",
        "Agentic AI",
        "A practical way to design tools an agent can call reliably: narrow schemas, "
        "typed errors, idempotency and a routing layer that knows when not to call.",
    ),
    "designing-agent-workflows-that-recover": (
        "geometry-builds-trust",
        "Designing Agent Workflows That Recover",
        "Agentic AI",
        "Failure is the normal case, not the exception. How planning, checkpoints, "
        "bounded retries and human-in-the-loop turns turn brittle demos into systems.",
    ),
    "guardrails-that-actually-hold": (
        "a-greener-workspace",
        "Guardrails That Actually Hold",
        "LLMOps & Guardrails",
        "Prompt rules are not controls. Structured outputs, input validation, tool "
        "permissions and audit trails are what make enterprise AI defensible.",
    ),
    "memory-state-and-checkpoints": (
        "materials-and-memory",
        "Memory, State and Checkpoints",
        "Agentic AI",
        "The difference between conversation history and agent memory, and how "
        "checkpointing state lets a long-running workflow resume instead of restarting.",
    ),
    "grounding-provenance-and-trust": (
        "the-creative-desk",
        "Grounding, Provenance and Trust",
        "RAG & Retrieval",
        "Groundedness is only useful if a reviewer can see where an answer came from. "
        "Source attribution, citations and hybrid retrieval explained.",
    ),
    "evaluation-is-the-product": (
        "the-power-of-focus",
        "Evaluation Is the Product",
        "LLMOps & Guardrails",
        "Offline eval datasets, retrieval metrics, groundedness scoring and regression "
        "tests are the only reason an LLM feature is allowed to keep shipping.",
    ),
}

# The three category enums are relabelled once, in the CMS schema bundle.
CATEGORY_LABELS = [
    ("Design", "Agentic AI"),
    ("Creativity", "RAG & Retrieval"),
    ("Workspace", "LLMOps & Guardrails"),
]

# Each post keeps the template's shape: 6 opening paragraphs, then three
# sections (h4 + 2 paragraphs, h4 + 1 paragraph, h4 + 1 paragraph).
POST_BODY = {
    "why-graphs-beat-flat-search": [
        "Vector search is very good at one thing: finding text that looks like the "
        "question. That is enough for a lot of documentation, and it stops being "
        "enough the moment a user asks about something that only exists as a "
        "relationship.",
        "A knowledge graph stores the other half of the picture. Entities become "
        "nodes, the statements about them become edges, and a query can walk those "
        "edges instead of hoping that the right sentence was embedded somewhere "
        "nearby.",
        "GraphRAG combines both. A conventional retriever finds candidate passages, "
        "a graph traversal expands them into related entities and their neighbours, "
        "and the language model receives a much smaller and much more relevant "
        "context than a raw top-k dump.",
        "The practical difference shows up in questions that require joining facts. "
        "Which policy applies to this member. Which service depends on that "
        "component. Who approved this exception and when. Pure vector retrieval "
        "answers these by hoping the answer is sitting in one chunk.",
        "The cost is real. Entity resolution, ontology decisions and traversal "
        "budgets are engineering work, not a library call. For a corpus that is "
        "mostly prose with light structure, graph enrichment adds latency and "
        "maintenance for very little gain.",
        "The honest conclusion is that graph structure pays for itself when the "
        "questions are relational. If your users mostly ask what a document says, "
        "keep the pipeline simple and spend the effort on chunking and reranking "
        "instead.",
        "Where graphs change the answer",
        "Graph traversal is most valuable when a single hop of context meaningfully "
        "narrows the search space. A policy document that mentions twenty services "
        "is far easier to answer once the graph tells you which three apply to this "
        "member, in this state, under this plan version.",
        "It also makes provenance easier. Because every retrieved fact arrives "
        "attached to an edge, you can walk back to the exact source document and the "
        "exact statement that supported the answer, rather than hoping the citation "
        "came from the right page.",
        "Where the simpler pipeline wins",
        "Start with vector search plus reranking and measure before you add a graph. "
        "Track groundedness and answer quality on a real evaluation set. If "
        "relationship questions are rare and the added latency is unacceptable, the "
        "graph is complexity without benefit.",
        "Whichever route you take, measure it. Retrieval quality is a property of "
        "the pipeline, not of the model, and it is the part of the system you can "
        "actually improve with evidence.",
        "Keep the graph small enough to reason about. A narrow ontology over the "
        "entities your questions actually join beats an elaborate one you cannot keep "
        "current, because a stale graph produces confidently wrong answers that look "
        "identical to correct ones.",
    ],
    "shipping-agents-to-production": [
        "A demo agent is easy. A demo agent answers one question, in one session, on "
        "a clean laptop, with nobody watching the bill. Production is where every "
        "one of those assumptions stops being true.",
        "The first thing that breaks is state. A user closes the tab halfway through "
        "a multi-step task and comes back tomorrow. If your agent keeps state only in "
        "memory, the work is lost and the retry starts from zero.",
        "The second thing that breaks is failure. Tools time out, models return "
        "malformed output, a downstream API rate-limits you at 3am. An agent without "
        "bounded retries and a defined fallback path will eventually decide from "
        "partial information, which is worse than failing.",
        "The third thing that breaks is cost. One badly planned loop can generate "
        "thousands of model calls before anyone notices. Token budgets, per-request "
        "ceilings and a hard stop on tool-call count are not optimisations, they are "
        "safety limits.",
        "The fourth thing that breaks is evaluation. Without a regression suite, "
        "every prompt change is a gamble, and nobody wants to be the person who "
        "silently degraded a workflow that customers depend on.",
        "The fifth thing that breaks is approval. Real enterprise actions need a "
        "human in the loop, and a human-in-the-loop path is something you design, "
        "not a checkbox you tick after the fact.",
        "What production actually needs",
        "Design the failure states before the happy path. Write down what the agent "
        "should do when a tool fails, when the model returns something unparseable, "
        "and when it runs out of budget. In most systems these branches carry more "
        "logic than the happy path does.",
        "Make every long-running step resumable. Persist the state that matters, "
        "attach an idempotency key to anything with side effects, and give the user "
        "a way to inspect what the agent believes is true right now.",
        "Ship behind a flag and watch the traces",
        "Run it on a small slice of real traffic first. Traces are worth more than "
        "logs here, because you need to see the reasoning path, not just the "
        "outcome. Alert on latency, cost per request and escalation rate, and give "
        "the team a way to replay a bad run.",
        "The teams that get this right treat the agent as a distributed system that "
        "happens to call a language model. That framing is unfashionable and "
        "completely correct.",
        "Start with a single agent and a narrow job. Multi-agent orchestration is a "
        "response to real routing and parallelism requirements, not a starting "
        "architecture, and every extra agent is another place for state to get lost.",
    ],
    "tool-calling-without-the-chaos": [
        "Tool calling is where agentic systems earn their keep and where they usually "
        "fall apart. The model is good at choosing a tool. Everything around the "
        "tool is where the real engineering is.",
        "The most common failure is a schema that is too broad. A tool with twenty "
        "optional parameters and vague descriptions gives the model a dozen equally "
        "plausible ways to be wrong, and every one of them costs a round trip.",
        "Narrow tools win. One tool with two or three required parameters and a clear "
        "description of when to use it beats a general-purpose API wrapper every "
        "time. If two workflows genuinely need different shapes, expose two tools.",
        "The second most common failure is treating errors as strings. Return "
        "structured errors with a machine-readable code and a message written for "
        "the model, not for your logs. The model can recover from a precise failure "
        "far more often than from a stack trace.",
        "The third is forgetting that tools have side effects. A read tool can be "
        "retried freely. A tool that writes needs an idempotency key, because the "
        "agent will eventually call it twice, and it should be safe when it does.",
        "The fourth is having no router. A good orchestration layer decides when to "
        "answer from context, when to retrieve, when to call a tool and when to stop. "
        "Without it, agents loop, because looping is the default behaviour of a "
        "model that wants to be helpful.",
        "Designing tools the model can actually use",
        "Write the tool description as if you were briefing a new joiner. State what "
        "the tool does, when to use it, when not to use it, and what the response "
        "means. Vague descriptions are the single biggest source of wasted tool "
        "calls in my experience.",
        "Return the smallest useful payload. Every token a tool returns is a token "
        "the model has to reason over, and every field it does not need is an "
        "opportunity to be distracted by it.",
        "Stop the loop explicitly",
        "Give the agent an explicit finish signal and a step budget. When it reaches "
        "either it should hand back what it has with an honest description of what "
        "is still unknown, rather than improvising a third tool call.",
        "Good tool design is unglamorous work: narrow schemas, precise errors, "
        "bounded retries and an honest stopping condition. It is also most of what "
        "separates a demo from something you would let a colleague depend on.",
        "Once a tool works reliably, version it. Tool signatures drift, agents get "
        "prompted against stale descriptions, and a breaking change to an argument "
        "name can quietly break workflows nobody owns any more.",
    ],
    "designing-agent-workflows-that-recover": [
        "Failure is the normal case in an agentic workflow. Models produce invalid "
        "output, tools time out, retrieved context contradicts itself, and the "
        "network disappears at the least convenient moment.",
        "A workflow that assumes the happy path is not resilient, it is lucky. "
        "Resilience comes from designing the recovery paths with the same care as the "
        "successful one.",
        "Planning is the first line of defence. Splitting a request into explicit "
        "steps, each with its own success condition, gives you somewhere to resume "
        "from and something meaningful to log when it breaks.",
        "Checkpointing is the second. Persist state after every meaningful step, not "
        "just at the end, so a failure at step six does not throw away the work from "
        "steps one to five. It also turns long-running workflows into something a "
        "user can leave and come back to.",
        "Bounded retries are the third. One retry handles a transient blip. Ten "
        "retries handle a design flaw and cost you a small fortune while doing it. "
        "Retry a specific failure class, with backoff, and give up into a defined "
        "fallback rather than an infinite loop.",
        "Human-in-the-loop is the fourth, and it is not a cop-out. When the agent is "
        "about to take an action that is expensive, irreversible or governed by "
        "policy, the correct design is to stop and ask, with the context already "
        "assembled.",
        "Recovery is a design decision, not an exception path",
        "Decide, per step, what happens when it fails. Some failures should abort. "
        "Some should skip to the next step and mark the result partial. Some should "
        "escalate to a human. A workflow that never makes this decision makes it by "
        "accident, at three in the morning.",
        "Make partial success a first-class state. If three of four sources were "
        "retrieved successfully, returning a grounded partial answer with an honest "
        "note about the gap is usually far more useful than failing the whole "
        "request.",
        "Test the ugly paths on purpose",
        "Your test suite should contain the cases that embarrass you: empty "
        "retrieval, contradictory sources, a tool that returns a 500, a model "
        "response that is valid JSON with the wrong shape. Those are the runs that "
        "happen in production.",
        "Teams that design recovery explicitly end up with agents that are boring in "
        "the best possible way. They fail visibly, they resume cleanly, and they "
        "never quietly invent an answer to cover a gap.",
        "Finally, rehearse the recovery paths on purpose. Fault injection against your "
        "own workflow is the cheapest way to find out whether a checkpoint actually "
        "restores what you think it restores.",
    ],
    "guardrails-that-actually-hold": [
        "A prompt is a suggestion. A guardrail is a control. Mixing the two up is how "
        "enterprise AI programmes end up with a security review that never quite "
        "finishes.",
        "The distinction matters because controls can be enforced and suggestions "
        "cannot. If an action must not happen, it belongs in code that validates the "
        "action, not in a paragraph at the top of a system prompt.",
        "Start at the edges. Validate and normalise every input before it reaches a "
        "model, because a model will happily process a prompt injection that you "
        "allowed to reach it in the first place.",
        "Then constrain the output. Structured outputs or a strict schema turn a "
        "free-text response into something you can parse, validate and reject. "
        "Unvalidated text from a model is untrusted input with better manners.",
        "Guard the tools separately. Prompt-level rules do not stop a tool call. "
        "Enforce permissions, argument validation and allow-lists in the tool layer, "
        "where the actual side effect happens.",
        "Finally, make it auditable. Log the inputs, the retrieved context, the tool "
        "calls and the final answer with identifiers that let you reconstruct the "
        "decision later. If you cannot replay a run, you cannot defend it.",
        "Controls that survive contact with production",
        "Validation at the boundary is the highest-value control there is. Type "
        "checks, size limits, encoding normalisation and content filtering catch a "
        "remarkable share of real problems before a single token is spent.",
        "Structured output plus a validator is the second. Parse, validate, and reject "
        "with a specific error the model can act on. Retrying a validation failure "
        "with the specific complaint works far better than retrying the original "
        "request.",
        "Human approval belongs to the action, not the workflow",
        "Define which actions require approval and enforce that boundary independently "
        "of what the model believes. A workflow that can talk itself past its own "
        "guardrails is not a governed system, however well the prompt is written.",
        "Good governance feels slower in the prototype and much faster in production. "
        "That is the whole trade, and it is a good one.",
        "Keep an inventory of what your system can actually do. Guardrails written "
        "against a capability list nobody maintains are a historical document, not a "
        "control, and the gap between the two is where incidents live.",
    ],
    "memory-state-and-checkpoints": [
        "Agent memory is one of those terms that means several different things. "
        "Sorting them out is most of the work.",
        "Conversation history is what the model has already been told this session. It "
        "grows linearly, it is expensive, and most of it stops being relevant within "
        "a few turns.",
        "Working state is what the workflow needs to remember in order to continue: "
        "which step completed, what the tool returned, which entity the user selected, "
        "what has already been written to a downstream system.",
        "Long-term memory is something you chose to persist across sessions, and it "
        "needs a schema. A list of facts with timestamps is a database, not a memory, "
        "and treating it as a memory is how you end up retrieving something that "
        "stopped being true months ago.",
        "Checkpointing sits across all three. It is the act of writing working state "
        "somewhere durable at a point where the workflow could resume, so that a "
        "failure costs you one step rather than the entire run.",
        "Resumability is the feature people are really buying. A user who closes the "
        "tab and comes back tomorrow should find their work intact, not an apologetic "
        "reset.",
        "Designing state that survives",
        "Make state serialisable and versioned. A checkpoint you cannot migrate is a "
        "checkpoint that will eventually crash on an old shape, and it will crash at "
        "the worst moment. Keep the schema small and treat it as an API.",
        "Give every external side effect an idempotency key derived from the run and "
        "the step. Retries are inevitable, and duplicate writes are not an acceptable "
        "consequence of them.",
        "Prune aggressively",
        "Decide what earns its place in long-term memory and what does not. Most "
        "conversation detail does not. Preferences, confirmed decisions and durable "
        "identifiers usually do, and everything else is storage cost plus retrieval "
        "noise.",
        "Memory that is written carefully and pruned on purpose is genuinely useful. "
        "Memory that accumulates by default is a liability that will eventually "
        "assert something false with complete confidence.",
        "Write memory down where the user can see it. Being able to inspect and correct "
        "what the system believes about them turns an opaque guess into a shared "
        "assumption, which is a much healthier place for an agent to operate from.",
    ],
    "grounding-provenance-and-trust": [
        "Groundedness is the claim that an answer came from the context you supplied. "
        "It is the property enterprise users care about most, and it is the one most "
        "often asserted without evidence.",
        "An answer can be perfectly grounded and still useless if the reader cannot "
        "tell where it came from. Provenance is what turns a plausible answer into "
        "something a person can act on.",
        "That means carrying source identifiers through the whole pipeline, not just "
        "at the end. Each retrieved chunk keeps its document, section and position. "
        "The generator receives them alongside the text. The response returns them.",
        "Attribution also constrains generation. Once every claim has to carry a "
        "source, unsupported claims become visible during development instead of "
        "during a customer escalation.",
        "Hybrid retrieval helps. Vector search finds language that matches; keyword "
        "and graph search find the exact entity, the policy number or the "
        "relationship that embedding models tend to blur. Running both and merging "
        "the results is more work and fewer surprises.",
        "Finally, measure groundedness on a labelled set rather than trusting it. "
        "Score whether each claim is supported by its cited source, and track that "
        "number as a release gate.",
        "Provenance has to survive the whole pipeline",
        "Chunk identifiers are the backbone. If a chunk cannot be traced back to a "
        "document and a location, nothing downstream can be made auditable, no matter "
        "how good the prompt is.",
        "Refuse to answer when the evidence is missing. A confident refusal with an "
        "explanation beats a plausible guess, especially in domains where being wrong "
        "has consequences. Users forgive a system that says no; they do not forgive "
        "one that invents.",
        "Make the reviewer the beneficiary",
        "Design for the person checking the answer rather than the person reading it. "
        "Citations that open the exact paragraph, timestamps for time-sensitive facts, "
        "and a visible distinction between retrieved fact and generated inference all "
        "reduce the cost of verification.",
        "Trust is not a tone of voice. It is a chain of evidence that someone can walk "
        "from the final sentence back to the source without taking anything on faith.",
        "None of this is exotic. It is the same discipline you would apply to a "
        "financial report, applied to a system that writes sentences instead of "
        "spreadsheets, and it is exactly as necessary.",
    ],
    "evaluation-is-the-product": [
        "Most LLM features are evaluated by whoever built them, on the examples they "
        "remember, immediately after a change. That is not evaluation. That is a vibe "
        "check with extra steps.",
        "The first thing a serious evaluation setup gives you is a dataset. A few "
        "hundred labelled cases covering the real distribution of questions, including "
        "the ugly ones: ambiguous phrasing, missing context, adversarial input, and "
        "questions with no good answer.",
        "The second is retrieval metrics. Hit rate and recall at k tell you whether "
        "the right context reached the model at all. Without them you cannot tell a "
        "retrieval problem from a generation problem, and you will spend weeks tuning "
        "prompts to fix a chunking bug.",
        "The third is groundedness and answer quality. Groundedness asks whether each "
        "claim is supported by the context. Answer quality asks whether it is correct "
        "and useful. They fail differently and they need different fixes.",
        "The fourth is regression testing. Every prompt, model or chunking change runs "
        "against the same suite, and a drop in score blocks the release. This is the "
        "single highest-leverage thing you can add to an AI product.",
        "The fifth is observability in production. Offline scores tell you about the "
        "dataset you thought of. Traces, feedback capture and error analysis tell you "
        "about the users you did not.",
        "What a workable evaluation loop looks like",
        "Keep the dataset in version control next to the code and review it like code. "
        "Add a case every time a real user hits something the system handled badly, "
        "and review it weekly. The suite should grow faster than the feature.",
        "Score with a mix of deterministic checks and model-based judging. Exact match "
        "and citation checks catch real regressions cheaply. Use a stronger model as "
        "the judge for semantic quality, calibrate it against human labels, and "
        "re-calibrate whenever the judge model changes.",
        "Gate the release, then watch production",
        "Define a small number of thresholds that block a deploy: groundedness, "
        "retrieval recall and the rate of escalations. Then keep sampling production "
        "traces against those same metrics, because the real distribution drifts and "
        "your dataset will not notice.",
        "The teams that treat evaluation as the product are the ones whose AI "
        "features get better over time instead of drifting. It is unglamorous work, "
        "and it is the work that compounds.",
        "Start with one hundred cases rather than a thousand. A small suite that runs "
        "on every change is worth more than a perfect one that only runs before a "
        "release, because the value of an evaluation set comes from how often it is "
        "consulted.",
    ],
}

IMAGE_ALTS = [
    ("Kh\u00f4ng gian l\u00e0m vi\u1ec7c c\u00f3 nhi\u1ec1u c\u00e2y xanh",
     "A workspace with plenty of greenery"),
    ("G\u00f3c l\u00e0m vi\u1ec7c y\u00ean t\u0129nh trong \u00e1nh s\u00e1ng d\u1ecbu",
     "A quiet corner of work in soft light"),
    ("Ki\u1ebfn tr\u00fac hi\u1ec7n \u0111\u1ea3i v\u1edbi c\u1ea5u tr\u00fac h\u00ecnh h\u1ec7c",
     "Modern architecture with geometric structure"),
    ("\u0110\u00e8n b\u00e0n tr\u1eafng trong kh\u00f4ng gian t\u1ed1i gi\u1ea3n",
     "A white desk lamp in a minimalist room"),
    ("Ng\u01b0\u1eddi ph\u1ee5 n\u1ee5 l\u00e0m vi\u1ec7c trong c\u0103n ph\u00f2ng t\u1ed1i gi\u1ea3n",
     "A person working in a minimalist room"),
    ("B\u00e0n l\u00e0m vi\u1ec7c v\u1edbi m\u00e1y t\u00ednh v\u00e0 nhi\u1ec1u t\u00e1c ph\u1ea7m ngh\u1ec7 thu\u1eadt",
     "A desk with a laptop and several artworks"),
    ("Kh\u00f4ng gian ki\u1ebfn tr\u00fac hi\u1ec7n \u0111\u1ea3i v\u1edbi chi ti\u1ebft g\u1ed7",
     "A modern architectural space with wooden details"),
    ("M\u00e1y t\u00ednh tr\u00ean b\u00e0n l\u00e0m vi\u1ec7c s\u00e1ng t\u1ea1o",
     "A laptop on a creative desk"),
]

# ------------------------------------------------------------------ projects
OLD_TITLES = {
    "a-greener-workspace": "A Greener Workspace",
    "beyond-the-screen": "Beyond the Screen",
    "everyday-beauty": "Everyday Beauty",
    "geometry-builds-trust": "Geometry Builds Trust",
    "ideas-need-silence": "Ideas Need Silence",
    "materials-and-memory": "Materials and Memory",
    "the-creative-desk": "The Creative Desk",
    "the-power-of-focus": "The Power of Focus",
}
_OLD_TITLES = OLD_TITLES

# Tags come first: "Enterprise GraphRAG" is a new project title that must not
# then be rewritten by the tag rule below.
PROJECT_TAGS = [
    ("Healthcare", "Healthcare AI"),
    ("Workflow Design", "GraphRAG"),
    ("SaaS", "Agentic AI"),
    ("Transformation", "Multi-Agent"),
    ("Proptech", "LLMOps"),
    ("0 -> 1", "Automation"),
    ("Strategy", "AI Strategy"),
    ("Enterprise", "Cloud"),
]

PROJECT_COPY = [
    ("Meridian Health", "Enterprise GraphRAG"),
    ("StyleBook", "Multi-Agent Copilot"),
    ("Homestead", "ExpertGPT Excel Agent"),
    ("North Light", "LLM Analysis Pipeline"),
    ("meridian-health", "enterprise-graphrag"),
    ("stylebook", "multi-agent-copilot"),
    ("homestead", "expertgpt-excel-agent"),
    ("north-light", "llm-analysis-pipeline"),
    ("When therapists spend less time clicking, they have more time for patients.",
     "Graph-enhanced retrieval that reasons across entities, relationships and "
     "multi-hop context."),
    ("From 'I hate this system' to 'Can we show other salons?",
     "Routing, tool calling and grounded retrieval orchestrated end to end with "
     "LangGraph."),
    ("Helping first-time homebuyers actually understand what they're looking at.",
     "LangChain tools and guardrails that cut manual reporting effort by about 60 "
     "percent."),
    ("Getting seven stakeholders to agree on what they're actually building.",
     "A reusable AWS pattern: SQS to Lambda router to S3 context to LLM to S3."),
    ("Product Designer", ROLE),
    ("2 Enginners, 1 PM, me", "2 Engineers, 1 PM"),
    ("a group of people ", "A knowledge graph rendered as connected nodes"),
    ("a man is thinking about things", "Several agents passing work between each other"),
    ("two dog in front of the house", "A spreadsheet turning into a generated report"),
    ("a man in the desert", "A serverless pipeline moving data between stages"),
]

PROJECT_MAP = dict(PROJECT_TAGS + PROJECT_COPY)

# -------------------------------------------------------------------- global
GLOBAL = [
    ("Nudge is a bold, personality-driven portfolio template for product designers "
     "who want to stand out. Built for storytelling, not just showcasing.",
     SITE_DESCRIPTION),
    ("Nudge - Premium Portfolio Template", HOME_TITLE),
    ("My Framer Site", NAME),

    ("I'm Bejaman", "I'm Amara"),
    ("I'm Bejaman ", "I'm Amara "),
    ("Bejaman", NAME),

    ("Case study", "Case Studies"),
    ("Open to contract work, full-time roles, and interesting conversations about "
     "hard design problems.",
     "Open to AI engineering consults, senior platform roles, and conversations about "
     "hard agentic problems."),
    ("I'm most energized by projects where I can dig into complex problems, "
     "collaborate with smart people, and ship things that genuinely improve "
     "someone's day.",
     "I'm most energized by systems where the model is only half the problem: "
     "retrieval has to ground it, evaluation has to catch it, and the whole thing "
     "has to survive production traffic."),
    ("hard design problems", "hard agentic problems"),

    # The template labels this section "Journal"; the route stays /blog.
    ("Journal", "Blog"),

    ("Facebook", "LinkedIn"),
    ("Instagram", "GitHub"),
    ("Linkedin", "Email"),
    # Order matters: the template's third social link points at a bare
    # linkedin.com and must become email first, otherwise the real LinkedIn
    # profile written in above would be rewritten a second time.
    ("https://www.linkedin.com/", CONTACT["email"]),
    ("https://www.facebook.com/", CONTACT["linkedin"]),
    ("https://www.instagram.com/", CONTACT["github"]),
    ("hello@example.com", "email-dineshkumar.amara@gmail.com"),
    ("mailto:Hello@selenadesigns.com", CONTACT["email"]),
    ("Hello@BEJAMANdesigns.com", EMAIL_DISPLAY),
    ("tel:+123456789", CONTACT["phone"]),
    ("+123456789", PHONE_DISPLAY),

    ("Currently at Meridian Health", "Currently at JPMorgan Chase"),
    ("Previously at Searchless AI", "Previously at Evernorth Health"),
    ("Product designer", ROLE),
    ("Chicago, IL", LOCATION),
    ("a product designer in Chicago who gets excited",
     "an AI engineer in Hyderabad who gets excited"),
    ("about making complicated things simple",
     "about turning unreliable models into dependable systems"),
    ("COntact me", "Contact me"),
    ("This is a showcase of what happens when curiosity drives the process.",
     "Selected systems I designed, built and put in front of real users."),
    ("nothing big, still feels nice", "nothing shipped, still learning"),

    # Footer monogram
    (">EM<", ">AD<"),
    (">PH<", ">AK<"),
    ("children:`EM`", "children:`AD`"),
    ("children:`PH`", "children:`AK`"),
]

# Copy scoped to a single page. Applied before GLOBAL so a shared string can
# mean different things on different pages.
SCOPED = {
    "index.html": [
        ("Available for thoughtful projects", "Available for agentic AI work"),
        ("outstanding digital products", "AI systems that ship"),
        ("Interaction Design", "Agentic AI"),
        ("Prototyping", "GraphRAG & RAG"),
        ("User Research", "LLM Evaluation"),
        ("Motion Design", "AWS & LLMOps"),
    ],
    "about.html": [
        ("I spend my days designing for healthcare platforms, booking systems, and "
         "other products where 'just figure it out' isn't an option. The people "
         "using these tools are busy, stressed, and have actual work to do. My job "
         "is to get out of their way.",
         "I build AI systems for regulated enterprises, where a plausible wrong "
         "answer costs more than no answer at all. The teams using these systems "
         "are busy and accountable, and the problems they face do not pause while a "
         "model thinks. My job is to make the system dependable enough that they can "
         "stop checking it."),
        ("I've worked on teams of two and teams of twenty. I've had access to endless "
         "user research and I've had to make educated guesses with limited data. I've "
         "worked within strict component libraries and I've built design systems "
         "from scratch. What stays consistent is asking good questions, collaborating "
         "with people who know more than me, and shipping things that actually help",
         "I have worked on teams of two and teams of twenty. I have had clean "
         "labelled datasets and I have had to build an evaluation set out of support "
         "tickets. I have inherited a prompt nobody wanted to touch and I have "
         "designed the retrieval layer from first principles. What stays consistent "
         "is measuring before claiming, collaborating with people who know more than "
         "me, and shipping systems that genuinely help"),
        ("Currently, I'm at Meridian Health working on experiences for mental health "
         "clinicians and administrators. Before that, I spent almost two years at "
         "StyleBook helping salons manage their businesses (and discovering that "
         "stylists have very strong opinions about scheduling interfaces, which I "
         "deeply respect).",
         "Currently I'm at JPMorgan Chase building enterprise AI/ML services across "
         "LLM applications, retrieval and evaluation. Before that I spent a year and "
         "a half at Evernorth Health Services, where I designed an enterprise GraphRAG "
         "solution and multi-agent copilots for healthcare knowledge. Earlier I led "
         "applied AI/ML research at Toshiba Software and spent seven years at Tata "
         "Consultancy Services building the software engineering foundations I still "
         "rely on."),
        ("When I'm not designing, you'll find me thinking about why some interfaces "
         "feel intuitive and others make you want to throw your laptop out a window. "
         "Usually with coffee.",
         "When I'm not shipping AI systems, you'll find me reading evaluation traces "
         "and arguing about whether a grounded answer is actually grounded. Usually "
         "with far too much coffee."),
        ("What dive into my work", "What I dive into my work"),
        ("Starting with why, not what", "Start with the failure, not the demo"),
        ("think first, draw later.", "measure before you claim."),
        ("Before jumping into wireframes, I want to understand what problem we're "
         "actually solving. Sometimes the thing people ask for isn't the thing they "
         "need. My favorite projects start with good questions and end with solutions "
         "that feel obvious in hindsight.",
         "Before writing a prompt I want to know how this fails in production. "
         "Sometimes the thing a stakeholder asks for is not the thing that breaks. My "
         "favourite projects start with a concrete failure and end with a system that "
         "behaves predictably under load."),
        ("no perfect world here!", "production has no happy path."),
        ("Perfect conditions don't exist. Budgets are tight, timelines are aggressive, "
         "legacy systems are messy, and sometimes you just can't talk to users "
         "directly. I'm comfortable making smart decisions with imperfect information "
         "and finding creative solutions within real limitations.",
         "Perfect conditions never exist. Latency budgets are tight, timelines are "
         "aggressive, legacy systems are messy, and sometimes the only labelled data "
         "you get is what support tickets tell you. I am comfortable making defensible "
         "decisions with imperfect information inside real constraints."),
        ("Collaboration over hero design", "Collaboration over hero models"),
        ("The best work happens when designers, engineers, and product folks are "
         "actually talking to each other\u2014not throwing things over the wall. I "
         "genuinely enjoy the back-and-forth of figuring out what's possible, what's "
         "practical, and what's going to create the most value.",
         "The best work happens when engineering, product and the business are "
         "actually in the same conversation instead of passing requirements over a "
         "wall. I genuinely enjoy working out what is possible, what is practical, "
         "and what will actually move a number that matters."),
        ("we, not me.", "platform, not prototype."),
        ("Making the invisible visible", "Making the invisible auditable"),
        ("Some of the most impactful design work isn't flashy\u2014it's the progress "
         "indicator that keeps people oriented, the auto-save that prevents panic, "
         "the validation message that actually helps instead of just saying 'error.' "
         "These details build trust.",
         "Some of the most valuable engineering work is not flashy. It is the "
         "provenance record that lets a reviewer check a claim, the retry that "
         "prevents a lost workflow, and the validation message that says what went "
         "wrong instead of just that something did. These details build trust."),
        ("details build trust.", "every answer needs a source."),
        (">StyleBook<", ">Evernorth Health Services<"),
        (">Meridian Health<", ">JPMorgan Chase<"),
        (">Northlight Consulting<", ">Toshiba Software<"),
        (">Homestead<", ">Tata Consultancy Services<"),
        ("Redesigned everything from appointment booking to inventory management for "
         "a salon management platform. Worked directly with salon owners and "
         "stylists to understand their workflows, then rebuilt features to match how "
         "they actually work instead of how we thought they worked.",
         "Designed and prototyped an enterprise GraphRAG solution combining knowledge "
         "graph concepts, entity and relationship modelling, semantic retrieval and "
         "LLM generation. Built multi-agent RAG and copilot systems with LangGraph, "
         "and an Excel reporting agent that cut manual effort by around 60 percent."),
        ("Led UX strategy and discovery for enterprise clients. Facilitated "
         "workshops with stakeholders who had very different ideas about what they "
         "were building, then helped everyone land on the same page. Also mentored "
         "junior designers, which taught me how to articulate my process instead of "
         "just doing it.",
         "Research analyst across AI/ML and R&D. Built deep learning, NLP, Transformer "
         "and generative AI solutions, designed knowledge-intensive RAG systems with "
         "hybrid retrieval and reranking, and worked on LoRA and QLoRA fine-tuning "
         "with PEFT. Turned research prototypes into reusable Python components."),
        ("Joined when the product was technically functional but deeply confusing. "
         "Talked to users who were struggling, mapped out where the interface was "
         "failing them, and redesigned the core experience to actually make sense. "
         "Also helped establish initial brand direction.",
         "Seven years building and supporting enterprise software and data solutions "
         "across client environments. Developed Python automation, data processing and "
         "ML workflows, and worked through requirements, implementation, testing and "
         "production support with cross-functional teams."),
        ("Sep 2025 - Current", "Feb 2026 - Present"),
        ("Mar 2024 - aug 2025", "Jul 2024 - Feb 2026"),
        ("Feb 2024 - dec 2024", "Aug 2021 - Jul 2024"),
        ("jan 2022 - dec 2023", "Oct 2014 - Aug 2021"),
    ],
"services.html": [
        ("available for Q4 projects ots", "available for AI work"),
        ("what I do", "what I build"),

        # Service blurbs (the 3rd and 4th share copy in the template).
        ("Designing digital products from the first idea to the final interface.",
         "Single and multi-agent systems built with LangGraph and LangChain: planning, "
         "routing, tool calling, memory and human-in-the-loop controls."),
        ("Strong visual direction with thoughtful structure to create digital "
         "experiences that are as effective as they are memorable",
         "GraphRAG, knowledge graphs and hybrid retrieval that ground answers in "
         "enterprise data, with provenance on every claim"),
        ("Building flexible visual systems that make products easier to design, build, "
         "and scale.",
         "LangSmith and Langfuse traces, evaluation datasets, groundedness scoring "
         "and regression tests wired into the release process.", 1),
        ("Building flexible visual systems that make products easier to design, build, "
         "and scale.",
         "AWS Bedrock, SageMaker, Lambda, SQS, Glue and EKS with Docker, Terraform and "
         "CI/CD behind every release, plus FastAPI services and reusable SDKs."),

        # Service tags.
        ("project strategy", "planning and routing"),
        ("prototyping", "tool calling"),
        ("Interaction Design", "human-in-the-loop"),
        ("design systems", "checkpointing"),
        ("Art Direction", "knowledge graphs", 1),
        ("Web design", "semantic search"),
        ("Responsive design", "hybrid retrieval"),
        ("Framer Development", "grounding &amp; citations"),
        ("Motion &amp; Interaction", "retrieval evaluation"),
        ("UI Systems", "observability"),
        ("Component Libraries", "regression testing"),
        ("Design tokens", "error analysis"),
        ("Documentation", "groundedness scoring"),
        ("System architecture", "LangSmith tracing"),
        ("Visual direction", "AWS Bedrock"),
        ("Brand Expression", "Docker &amp; Kubernetes"),
        ("Creative Strategy", "Terraform &amp; CI/CD"),
        ("Art Direction", "Serverless"),
        ("Design Leadership", "guardrails &amp; audit"),

        # Process.
        ("children:`Discover`", "children:`Assess`"),
        (">Discover<", ">Assess<"),
        ("children:`Define`", "children:`Architect`"),
        (">Define<", ">Architect<"),
        ("children:`Design`", "children:`Build`"),
        (">Design<", ">Build<"),
        ("children:`Deliver`", "children:`Operate`"),
        (">Deliver<", ">Operate<"),
        ("First, I get familiar with the problem, the people, and the bigger picture.",
         "First I understand the failure mode, the users, and the data the system is "
         "allowed to see."),
        ("I translate what I learn into a clear direction, structure, and set of "
         "priorities.",
         "Then I turn that into an architecture, an evaluation plan, and a set of "
         "explicit non-goals."),
        ("Then I explore, iterate, and refine until the right solution starts to take "
         "shape.",
         "Then I build it properly: orchestrations, retrieval pipelines, tools and "
         "guardrails, measured as I go."),
        ("Finally, I bring everything together into a polished, flexible system ready "
         "to ship.",
         "Finally it ships with traces, regression tests, cost ceilings and a runbook "
         "the team can actually operate."),

        # Capability marquee.
        ("UX / UI Design", "Agentic AI"),
        ("Product Strategy", "AI roadmap"),
        ("Design Strategy", "System design"),
        ("Information Architecture", "Knowledge graphs"),
        ("Research", "Agent architecture"),
        ("User Flows", "LLM fine-tuning"),
        ("UX Design", "Retrieval pipelines"),
        ("UI Design", "Guardrails"),
        ("Web Design", "FastAPI services"),
        ("Design Systems", "LLM evaluation"),
        ("Design Tokens", "Terraform"),
        ("Responsive Design", "LangSmith tracing"),
        ("Micro-interactions", "OpenTelemetry"),
        ("Motion Direction", "Model selection"),
        ("Transitions", "Cost tuning"),
        ("Prototyping", "evaluation suites", 1),
        ("Prototyping", "Reusable SDKs"),
        ("rTmzt9Hxo:`design`", "rTmzt9Hxo:`Delivery`"),
        (">design<", ">Delivery<"),
        ("rTmzt9Hxo:`Motion`", "rTmzt9Hxo:`Operations`"),
        (">Motion<", ">Operations<"),

        # FAQ.
        (">User<", ">Question<"),
        ("Does Bejaman design websites, or only digital products?",
         "Do you build agents, or only retrieval pipelines?"),
        ("Both. Alongside app/dashboard product design, Bejaman also designs websites "
         "and landing pages with a storytelling approach, not just visuals.",
         "Both, and they usually end up in the same system. A useful agent needs "
         "grounded retrieval, and a useful retrieval pipeline usually needs an "
         "orchestration layer to decide when to search and when to answer."),
        ("Does he build Design Systems, or just individual screens?",
         "Do you do evaluation, or only build features?"),
        ("Yes. Especially for multi stakeholder enterprise work like North Light, "
         "where a shared design language and reusable components are key to scaling "
         "the product.",
         "Yes. Without an evaluation set, every prompt or model change is a gamble. I "
         "build labelled datasets, retrieval metrics and regression tests before the "
         "feature, not after the first incident."),
        ("What does the Product Design process look like?",
         "What does an engagement actually look like?"),
        ("Four pillars: User Research to find the real problem, Interaction Design to "
         "shape the flow, Prototyping to test ideas fast, and Motion Design to polish "
         "the experience. Meridian Health and StyleBook are good examples of this in "
         "action.",
         "Four phases: understand the failure, design the architecture and the "
         "evaluation plan, build the orchestration and retrieval with guardrails in "
         "place, then ship behind monitoring with regression tests on every change."),
        ("What does Creative Direction mean here?",
         "What happens when the work is sensitive or regulated?"),
        ("It's guiding the overall visual identity, tone, and experience across a "
         "project, making sure every design decision (color, motion, storytelling) "
         "stays consistent and serves the client's business goals.",
         "Inputs get validated at the boundary, outputs are schema-constrained and "
         "re-validated, tool permissions are enforced in code rather than in the "
         "prompt, and every run is auditable with human approval on sensitive "
         "actions."),
    ],
    "contact.html": [
        ("Where to find you?", "Where can I reach you?"),
        ("What's on your mind?", "What are you building?"),
        ("I'm available for new projects!", "Open to AI engineering work!"),
        ("take a photos of a man", "Abstract contact illustration"),
    ],
}

# Extra copy that only exists inside a page's own JS module (no HTML equivalent).
SCOPED_JS = {
    "about.html": [
        ("children:`StyleBook`", "children:`Evernorth Health Services`"),
        ("children:`Meridian Health`", "children:`JPMorgan Chase`"),
        ("children:`Northlight Consulting`", "children:`Toshiba Software`"),
        ("children:`Homestead`", "children:`Tata Consultancy Services`"),
    ],
    "index.html": [
        ("children:`Available for thoughtful projects`",
         "children:`Available for agentic AI work`"),
        ("children:`outstanding digital products`",
         "children:`AI systems that ship`"),
    ],
    "services.html": [
        ("children:`what I do`", "children:`what I build`"),
    ],
}

# JS module that belongs to exactly one page.
PAGE_MODULE = {
    "about.html": "js/ebcpkwnxlarqv7nwmwepjkjnomhrdsoje0je1g8eyp0.biwafclo.mjs",
    "index.html": "js/tkk4bi1iemomfz2oee9rm5ng3bq8slljdvdots2wd04.bqv6p3lp.mjs",
    "services.html": "js/vigvwilqjzb1djayrjmh49b9ow6pb13oxhnqjngdpoe.b99-ycho.mjs",
    "case-study.html": "js/dcziej1zotbadg7gaz8towvzxevwmiluwxwjjn_9j9a.chf7himz.mjs",
    "contact.html": "js/btp3pvf_fyto_pg8rsb-hb_aafqbk-txzqyb0k7exy4.wieqap3q.mjs",
    "play-ground.html":
        "js/j_-9uoqg2t5mg7ylaFcQM2FcQs9cI0r7te9LDoin8wY.blouylt5.mjs",
    "blog/index.html":
        "js/va9yy_jaxpmftwl-rqsud5s0o4zf9yarhnbip8mo8aw.cdf0h2yy.mjs",
}
MODULE_TO_PAGE = {v: k for k, v in PAGE_MODULE.items()}

# Per-character animation runs rendered by Framer's split-text code component.
SPLIT = {
    "index.html": [
        ("Bejaman", NAME),
        ("Available for thoughtful projects", "Available for agentic AI work"),
        ("outstanding digital products", "AI systems that ship"),
        ("Meridian Health", "Enterprise GraphRAG"),
        ("When therapists spend less time clicking, they have more time for patients.",
         "Graph-enhanced retrieval that reasons across entities, relationships and "
         "multi-hop context."),
        ("StyleBook", "Multi-Agent Copilot"),
        ("From 'I hate this system' to 'Can we show other salons?",
         "Routing, tool calling and grounded retrieval orchestrated end to end with "
         "LangGraph."),
        ("Homestead", "ExpertGPT Excel Agent"),
        ("Helping first-time homebuyers actually understand what they're looking at.",
         "LangChain tools and guardrails that cut manual reporting effort by about 60 "
         "percent."),
        ("North Light", "LLM Analysis Pipeline"),
        ("Getting seven stakeholders to agree on what they're actually building.",
         "A reusable AWS pattern: SQS to Lambda router to S3 context to LLM to S3."),
    ],
    "case-study.html": [
        ("Meridian Health", "Enterprise GraphRAG"),
        ("When therapists spend less time clicking, they have more time for patients.",
         "Graph-enhanced retrieval that reasons across entities, relationships and "
         "multi-hop context."),
        ("StyleBook", "Multi-Agent Copilot"),
        ("From 'I hate this system' to 'Can we show other salons?",
         "Routing, tool calling and grounded retrieval orchestrated end to end with "
         "LangGraph."),
        ("Homestead", "ExpertGPT Excel Agent"),
        ("Helping first-time homebuyers actually understand what they're looking at.",
         "LangChain tools and guardrails that cut manual reporting effort by about 60 "
         "percent."),
        ("North Light", "LLM Analysis Pipeline"),
        ("Getting seven stakeholders to agree on what they're actually building.",
         "A reusable AWS pattern: SQS to Lambda router to S3 context to LLM to S3."),
    ],
    "services.html": [
        ("what i do", "what I build"),
        ("what I do", "what I build"),
        ("Product Design", "Agentic AI"),
        ("UX / UI Design", "Agentic AI"),
        ("web design", "RAG systems"),
        ("Design systems", "LLM evaluation"),
        ("Creative direction", "Cloud & LLMOps"),
        ("I'm most energized by projects where I can dig into complex problems, "
         "collaborate with smart people, and ship things that genuinely improve "
         "someone's day.",
         "The model is the easy part. The work is orchestration, grounding, "
         "evaluation and the guardrails that let an enterprise trust the output."),
    ],
}

# Journal post titles are animated per character on the post page.
for _slug, _data in POSTS.items():
    SPLIT.setdefault("blog/%s.html" % _slug, []).append(
        (_OLD_TITLES[_data[0]], _data[1]))


# ------------------------------------------------------------------ socials
# Contact page: three circular icon links whose glyphs were the template's
# Facebook / Instagram / LinkedIn paths. Corrected here, plus Scholar and
# Phone buttons cloned from the GitHub block.
ICON_FB = 'M12 2.04004C6.5 2.04004 2 6.53004 2 12.06C2 17.06 5.66 21.21 10.44 21.96V14.96H7.9V12.06H10.44V9.85004C10.44 7.34004 11.93 5.96004 14.22 5.96004C15.31 5.96004 16.45 6.15004 16.45 6.15004V8.62004H15.19C13.95 8.62004 13.56 9.39004 13.56 10.18V12.06H16.34L15.89 14.96H13.56V21.96C15.9164 21.5879 18.0622 20.3856 19.6099 18.5701C21.1576 16.7546 22.0053 14.4457 22 12.06C22 6.53004 17.5 2.04004 12 2.04004Z'
ICON_IG = 'M13.0276 2C14.1526 2.003 14.7236 2.009 15.2166 2.023L15.4106 2.03C15.6346 2.038 15.8556 2.048 16.1226 2.06C17.1866 2.11 17.9126 2.278 18.5496 2.525C19.2096 2.779 19.7656 3.123 20.3216 3.678C20.8303 4.17773 21.2238 4.78247 21.4746 5.45C21.7216 6.087 21.8896 6.813 21.9396 7.878C21.9516 8.144 21.9616 8.365 21.9696 8.59L21.9756 8.784C21.9906 9.276 21.9966 9.847 21.9986 10.972L21.9996 11.718V13.028C22.002 13.7574 21.9944 14.4868 21.9766 15.216L21.9706 15.41C21.9626 15.635 21.9526 15.856 21.9406 16.122C21.8906 17.187 21.7206 17.912 21.4746 18.55C21.2238 19.2175 20.8303 19.8223 20.3216 20.322C19.8219 20.8307 19.2171 21.2242 18.5496 21.475C17.9126 21.722 17.1866 21.89 16.1226 21.94L15.4106 21.97L15.2166 21.976C14.7236 21.99 14.1526 21.997 13.0276 21.999L12.2816 22H10.9726C10.2429 22.0026 9.51312 21.9949 8.78359 21.977L8.58959 21.971C8.3522 21.962 8.11487 21.9517 7.87759 21.94C6.81359 21.89 6.08759 21.722 5.44959 21.475C4.78242 21.2241 4.17803 20.8306 3.67859 20.322C3.16954 19.8224 2.7757 19.2176 2.52459 18.55C2.27759 17.913 2.10959 17.187 2.05959 16.122L2.02959 15.41L2.02459 15.216C2.00616 14.4868 1.99782 13.7574 1.99959 13.028V10.972C1.99682 10.2426 2.00416 9.5132 2.02159 8.784L2.02859 8.59C2.03659 8.365 2.04659 8.144 2.05859 7.878C2.10859 6.813 2.27659 6.088 2.52359 5.45C2.77529 4.7822 3.16982 4.17744 3.67959 3.678C4.17875 3.16955 4.78278 2.77607 5.44959 2.525C6.08759 2.278 6.81259 2.11 7.87759 2.06C8.14359 2.048 8.36559 2.038 8.58959 2.03L8.78359 2.024C9.51278 2.00623 10.2422 1.99857 10.9716 2.001L13.0276 2ZM11.9996 7C10.6735 7 9.40174 7.52678 8.46406 8.46447C7.52638 9.40215 6.99959 10.6739 6.99959 12C6.99959 13.3261 7.52638 14.5979 8.46406 15.5355C9.40174 16.4732 10.6735 17 11.9996 17C13.3257 17 14.5974 16.4732 15.5351 15.5355C16.4728 14.5979 16.9996 13.3261 16.9996 12C16.9996 10.6739 16.4728 9.40215 15.5351 8.46447C14.5974 7.52678 13.3257 7 11.9996 7ZM11.9996 9C12.3936 8.99993 12.7837 9.07747 13.1477 9.22817C13.5117 9.37887 13.8424 9.5998 14.1211 9.87833C14.3997 10.1569 14.6207 10.4875 14.7715 10.8515C14.9224 11.2154 15 11.6055 15.0001 11.9995C15.0002 12.3935 14.9226 12.7836 14.7719 13.1476C14.6212 13.5116 14.4003 13.8423 14.1218 14.121C13.8432 14.3996 13.5126 14.6206 13.1486 14.7714C12.7847 14.9223 12.3946 14.9999 12.0006 15C11.2049 15 10.4419 14.6839 9.87927 14.1213C9.31666 13.5587 9.00059 12.7956 9.00059 12C9.00059 11.2044 9.31666 10.4413 9.87927 9.87868C10.4419 9.31607 11.2049 9 12.0006 9M17.2506 5.5C16.9191 5.5 16.6011 5.6317 16.3667 5.86612C16.1323 6.10054 16.0006 6.41848 16.0006 6.75C16.0006 7.08152 16.1323 7.39946 16.3667 7.63388C16.6011 7.8683 16.9191 8 17.2506 8C17.5821 8 17.9001 7.8683 18.1345 7.63388C18.3689 7.39946 18.5006 7.08152 18.5006 6.75C18.5006 6.41848 18.3689 6.10054 18.1345 5.86612C17.9001 5.6317 17.5821 5.5 17.2506 5.5Z'
ICON_LI = 'M19.771 2.00928C20.3599 2.00928 20.9246 2.24319 21.3409 2.65955C21.7573 3.07591 21.9912 3.64061 21.9912 4.22944V19.7706C21.9912 20.3594 21.7573 20.9241 21.3409 21.3405C20.9246 21.7568 20.3599 21.9907 19.771 21.9907H4.22993C3.6411 21.9907 3.0764 21.7568 2.66004 21.3405C2.24367 20.9241 2.00977 20.3594 2.00977 19.7706V4.22944C2.00977 3.64061 2.24367 3.07591 2.66004 2.65955C3.0764 2.24319 3.6411 2.00928 4.22993 2.00928H19.771ZM19.216 19.2155V13.3321C19.216 12.3723 18.8347 11.4518 18.1561 10.7732C17.4774 10.0945 16.5569 9.71323 15.5971 9.71323C14.6536 9.71323 13.5546 10.2905 13.0218 11.1563V9.92415H9.92464V19.2155H13.0218V13.7428C13.0218 12.8881 13.71 12.1887 14.5648 12.1887C14.9769 12.1887 15.3722 12.3524 15.6637 12.6439C15.9551 12.9354 16.1189 13.3306 16.1189 13.7428V19.2155H19.216ZM6.31688 8.18132C6.81149 8.18132 7.28584 7.98484 7.63559 7.6351C7.98533 7.28535 8.18181 6.811 8.18181 6.31639C8.18181 5.28401 7.34925 4.44035 6.31688 4.44035C5.81932 4.44035 5.34214 4.63801 4.99032 4.98983C4.63849 5.34166 4.44084 5.81883 4.44084 6.31639C4.44084 7.34876 5.2845 8.18132 6.31688 8.18132ZM7.85989 19.2155V9.92415H4.78497V19.2155H7.85989Z'
ICON_BRACKETS = "M8.5 5.5 2.5 12l6 6.5 1.9-1.9-4.1-4.6 4.1-4.6L8.5 5.5zM15.5 5.5l6 6.5-6 6.5-1.9-1.9 4.1-4.6-4.1-4.6 1.9-1.9zM13.6 4.2l-2.9 15.6 1.9.5 2.9-15.6-1.9-.5z"
ICON_ENVELOPE = "M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2zm0 2.7l-.7.5L12 12.4 4.7 7.2 4 6.7V6l8 5 8-5v.7z"
ICON_CAP = "M12 3 1 9l11 6 8.6-4.7V15h2.1V9L12 3zM6.5 14.3V18c0 1.2 2.5 2.2 5.5 2.2s5.5-1 5.5-2.2v-3.7L12 17l-5.5-2.7z"
ICON_PHONE = "M7 2h10a2 2 0 012 2v16a2 2 0 01-2 2H7a2 2 0 01-2-2V4a2 2 0 012-2z"
ICON_PHONE_HOLE = "M6.2 6.2h11.6V17H6.2V6.2zM11 17.6h2v1.4h-2v-1.4z"

SOCIAL_NEW = [
    ("Scholar", "https://scholar.google.co.in/citations?user=ifPShVAAAAAJ&hl=en", "gScholar01"),
    ("Phone", "tel:+919629956726", "PhoneBtn02"),
]

SOCIAL_GH_ID = 'fz20ZnGn7'
SOCIAL_GH_CLASS = 'framer-1sqh48a-container'
SOCIAL_EMAIL_ID = 'itzdN9aaX'
SOCIAL_EMAIL_CLASS = 'framer-nm8fhl-container'

BUY_NUDGE_RE = re.compile(r"(text:`BUY NUDGE`.*?visible:)!0")
POLAR_ANCHOR_RE = re.compile(r'<a\b[^>]*buy\.polar\.sh[\s\S]*?</a>')


def _swap_icon_paths(text, email_anchor):
    """Point each social button at the right glyph."""
    i = text.find(email_anchor)
    if i >= 0:
        j = text.find(ICON_LI, i)
        if j >= 0:
            text = text[:j] + ICON_ENVELOPE + text[j + len(ICON_LI):]
    if ICON_FB in text:
        text = text.replace(ICON_FB, ICON_LI, 1)
    if ICON_IG in text:
        text = text.replace(ICON_IG, ICON_BRACKETS, 1)
    return text


def _clone_socials_bundle(text):
    i_gh = text.find(SOCIAL_GH_CLASS)
    if i_gh < 0:
        return text
    z_gh = text.rfind('s(z,{breakpoint:T,', 0, i_gh)
    i_em = text.find(SOCIAL_EMAIL_CLASS)
    z_em = text.rfind('s(z,{breakpoint:T,', 0, i_em) if i_em >= 0 else -1
    if z_gh < 0 or z_em <= z_gh:
        return text
    template = text[z_gh:z_em]
    clones = []
    for label, href, nid in SOCIAL_NEW:
        if nid in text:
            raise SystemExit('social id collision: ' + nid)
        c = template.replace(SOCIAL_GH_ID, nid)
        c = c.replace(CONTACT["github"], href)
        c = c.replace('VyONsZJ7g:`GitHub`', 'VyONsZJ7g:`%s`' % label)
        if label == 'Phone':
            c = c.replace('<path d="' + ICON_BRACKETS + '"', '<path fill-rule="evenodd" d="' + ICON_PHONE + '"')
            c = c.replace('M13.6 4.2l-2.9 15.6 1.9.5 2.9-15.6-1.9-.5z', ICON_PHONE_HOLE)
        elif label == 'Scholar':
            c = c.replace(ICON_BRACKETS, ICON_CAP)
        clones.append(c)
    return text[:z_em] + ''.join(clones) + text[z_em:]


def _clone_socials_html(html):
    i_gh = html.find(SOCIAL_GH_CLASS)
    if i_gh < 0:
        return html
    gh = html.rfind('<div class="ssr-variant">', 0, i_gh)
    i_em = html.find(SOCIAL_EMAIL_CLASS)
    em = html.rfind('<div class="ssr-variant">', 0, i_em) if i_em >= 0 else -1
    if gh < 0 or em <= gh:
        return html
    template = html[gh:em]
    clones = []
    for label, href, nid in SOCIAL_NEW:
        c = template.replace(CONTACT["github"], href)
        c = c.replace('>GitHub<', '>%s<' % label)
        if label == 'Phone':
            c = c.replace('<path d="' + ICON_BRACKETS + '"', '<path fill-rule="evenodd" d="' + ICON_PHONE + '"')
            c = c.replace('M13.6 4.2l-2.9 15.6 1.9.5 2.9-15.6-1.9-.5z', ICON_PHONE_HOLE)
        elif label == 'Scholar':
            c = c.replace(ICON_BRACKETS, ICON_CAP)
        clones.append(c)
    return html[:em] + ''.join(clones) + html[em:]


def fix_contact_socials(text, is_bundle):
    email_anchor = SOCIAL_EMAIL_ID if is_bundle else SOCIAL_EMAIL_CLASS
    text = _swap_icon_paths(text, email_anchor)
    if is_bundle:
        return _clone_socials_bundle(text)
    return _clone_socials_html(text)


def hide_template_chrome(html):
    """Drop the template upsell button from the SSR; CSS hides the badge."""
    return POLAR_ANCHOR_RE.sub('', html)


CHROME_CSS = (
    '<style data-site-chrome>#__framer-badge-container{display:none!important}'
    'a[href*=\"buy.polar.sh\"]{display:none!important}'
    '.framer-15ncfh8{flex-wrap:wrap!important}'
    '</style>'
)



RESUME_FILE = "/Amara_Dinesh_Kumar_Senior_AI_Engineer.pdf"

# Framer's "Made with Framer" badge and "Buy this template" button are hidden
# rather than deleted: the runtime still mounts both into the badge container,
# and removing the mount point makes React throw. The runtime rewrites <head> on
# every route, so the resume banner is injected after the mount point instead.
RESUME_BANNER = (
    '<div id="__framer-badge-container"></div>'
    '<div data-site-resume>'
    '<a href="%s" download>Download résumé</a>'
    '</div>' % RESUME_FILE
)

CONTACT_LINKS = (
    '<div data-site-contact>'
    '<a href="%s">%s</a>'
    '<a href="%s">%s</a>'
    '<a href="%s">LinkedIn</a>'
    '<a href="%s">GitHub</a>'
    '<a href="%s">Google Scholar</a>'
    '</div>'
) % (CONTACT["email"], EMAIL_DISPLAY, CONTACT["phone"], PHONE_DISPLAY,
     CONTACT["linkedin"], CONTACT["github"], CONTACT["scholar"])

CHROME_CSS = (
    '<style data-site-chrome>'
    '#__framer-badge-container{display:none!important}'
    'a[href*="buy.polar.sh"],a[href*="www.framer.com"]{display:none!important}'
    'a[href*="play-ground"]{display:none!important}'
    '[data-site-resume]{position:fixed;right:20px;bottom:20px;z-index:9999}'
    '[data-site-resume] a{display:inline-block;padding:12px 22px;'
    'border:1px solid #111212;border-radius:999px;background:#111212;color:#fff;'
    'font:500 15px/1 Inter,sans-serif;text-decoration:none;'
    'transition:transform .15s ease}'
    '[data-site-resume] a:hover{transform:translateY(-2px)}'
    '[data-site-contact]{display:flex;flex-wrap:wrap;gap:12px;'
    'justify-content:center;margin:48px auto 0;padding:0 24px;max-width:900px}'
    '[data-site-contact] a{flex:0 1 auto;padding:12px 22px;'
    'border:1px solid #111212;border-radius:999px;color:#111212;'
    'font:500 15px/1 Inter,sans-serif;text-decoration:none;'
    'transition:background .15s ease,color .15s ease}'
    '[data-site-contact] a:hover{background:#111212;color:#fff}'
    '</style>'
)

PLAYGROUND_ANCHOR_RE = re.compile(
    r'<a\b[^>]*href="/play-ground".*?</a>', re.S
)


def drop_playground_link(html):
    """Remove the Playground nav item.

    The item is authored in a shared nav component, so it is dropped from the
    SSR and hidden with CSS for the client-rendered copy.
    """
    return PLAYGROUND_ANCHOR_RE.sub("", html)


PORTRAIT_BUNDLE_IMG = (
    "images:[`../images/m2ikrrxfhsxjyxqcmhtrp56ia.png?width=382&height=456`,"
)
PORTRAIT_HTML_IMG = re.compile(
    r'<span style="display:inline-flex;[^"]*">'
    r'<img src="/images/m2ikrrxfhsxjyxqcmhtrp56ia\.png[^"]*"[^>]*>'
    r'</span>'
)


def drop_inline_portrait(text):
    """Remove the stock portrait the template inlines after "I'm Amara".

    The image is an emoji slot inside a rich-text line, so its placeholder has
    to go too, otherwise the remaining emoji shift by one.
    """
    if PORTRAIT_BUNDLE_IMG in text:
        text = text.replace(PORTRAIT_BUNDLE_IMG, "images:[", 1)
        return text.replace("I'm Amara [] ", "I'm Amara ", 1)
    return PORTRAIT_HTML_IMG.sub("", text)


# --------------------------------------------------------------------- engine
def _norm(pair):
    """(old, new) or (old, new, nth) -> (old, new, nth|None)."""
    if len(pair) == 3:
        return pair
    return (pair[0], pair[1], None)


def _variants(pair):
    """(search, replace, nth) pairs covering every escaping used on the site."""
    old, new, nth = _norm(pair)
    pairs = [(old, new, nth)]
    if "'" in old:
        pairs.append((old.replace("'", "&#39;"), new.replace("'", "&#39;"), nth))
        pairs.append((old.replace("'", "&apos;"), new.replace("'", "&apos;"), nth))
    if '"' in old:
        pairs.append((old.replace('"', "&quot;"), new.replace('"', "&quot;"), nth))
    return pairs


def _replace_nth(text, old, new, nth):
    index = -1
    for _ in range(nth):
        index = text.find(old, index + 1)
        if index == -1:
            return text
    return text[:index] + new + text[index + len(old):]


BARE_GITHUB_RE = re.compile(r"https://github\.com/(?![\w-])")


def _sub(text, pairs):
    for pair in pairs:
        old, new, nth = _norm(pair)
        if not old or old == new or old not in text:
            continue
        text = text.replace(old, new) if nth is None else \
            _replace_nth(text, old, new, nth)
    # github.com/<something> is already a real profile (or the instagram
    # rewrite above); only the bare template link still needs replacing, and a
    # plain substring swap would match inside the rewritten URL a second time.
    text = BARE_GITHUB_RE.sub(CONTACT["github"], text)
    return text


# ------------------------------------------------------------- split rich text
RICH_GROUP = re.compile(
    r'(<span style="white-space:nowrap">)'
    r'((?:<span style="display:inline-block;[^"]*">[^<]*</span>)+)'
    r'(</span>)'
)
CHAR_SPAN = re.compile(r'>([^<]*)</span>')


def replace_split(html, old, new):
    """Rewrite a per-character animation run so the SSR text matches the bundle."""
    old_words = old.split(" ")
    new_words = new.split(" ")
    groups = _groups(html)
    texts = [CHAR_SPAN.findall(g[2]) for g in groups]
    texts = ["".join(t) for t in texts]

    cursor = 0
    while cursor < len(groups):
        window = texts[cursor:cursor + len(old_words)]
        if window != old_words:
            cursor += 1
            continue
        style = re.search(
            r'<span style="display:inline-block;([^"]*)">[^<]*</span>', groups[cursor][2])
        if style is None:
            cursor += 1
            continue
        made = []
        for word in new_words:
            chars = "".join(
                '<span style="display:inline-block;%s">%s</span>'
                % (style.group(1),
                   c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
                for c in word
            )
            made.append('<span style="white-space:nowrap">%s</span>' % chars)
        blob = " ".join(made)
        a = groups[cursor][0]
        b = groups[cursor + len(old_words) - 1][1]
        html = html[:a] + blob + html[b:]
        groups = _groups(html)
        texts = ["".join(CHAR_SPAN.findall(g[2])) for g in groups]
        cursor += len(old_words)
    return html


def _groups(html):
    return [(m.start(2), m.end(2), m.group(2)) for m in RICH_GROUP.finditer(html)]


# ------------------------------------------------------------------- journal
_JOURNAL = None


def journal_pairs():
    """Flattened old -> new copy implied by POSTS, POST_BODY and the summaries."""
    global _JOURNAL
    if _JOURNAL is not None:
        return _JOURNAL

    pairs = []
    for new_slug, (src, title, category, summary) in POSTS.items():
        pairs.append((src, new_slug))
        path = os.path.join(SRC_ROOT, "blog", src)
        raw = open(path, encoding="utf-8").read()
        m = re.search(
            r'<script type="framer/handover" id="__framer__handoverData">(.*?)</script>',
            raw, re.S)
        olds = []
        for value in json.loads(m.group(1)):
            if isinstance(value, str) and value.startswith("[1,[4,"):
                for node in json.loads(value)[1:]:
                    child = node[3]
                    if (isinstance(child, list) and len(child) == 2
                            and child[0] == 5):
                        olds.append(child[1])
        news = POST_BODY[new_slug]
        if len(olds) != len(news):
            raise SystemExit("%s: %d source blocks, %d new blocks"
                             % (src, len(olds), len(news)))
        pairs.extend(zip(olds, news))

    # Titles and summaries are CMS scalars.
    src_titles = {
        "a-greener-workspace": "A Greener Workspace",
        "beyond-the-screen": "Beyond the Screen",
        "everyday-beauty": "Everyday Beauty",
        "geometry-builds-trust": "Geometry Builds Trust",
        "ideas-need-silence": "Ideas Need Silence",
        "materials-and-memory": "Materials and Memory",
        "the-creative-desk": "The Creative Desk",
        "the-power-of-focus": "The Power of Focus",
    }
    for new_slug, (src, title, category, summary) in POSTS.items():
        old_title = src_titles[src]
        pairs.append((old_title, title))
        raw = open(os.path.join(SRC_ROOT, "blog", src), encoding="utf-8").read()
        old_summary = _handover_scalar(raw, src)
        pairs.append((old_summary, summary))

    pairs.extend(IMAGE_ALTS)
    _JOURNAL = pairs
    return pairs


def _handover_scalar(raw, slug):
    """The post summary, read straight out of the export's handover payload."""
    m = re.search(
        r'<script type="framer/handover" id="__framer__handoverData">(.*?)</script>',
        raw, re.S)
    data = json.loads(m.group(1))
    for i, value in enumerate(data):
        if value != "enum":
            continue
        for candidate in data[i + 1:i + 10]:
            if (isinstance(candidate, str) and len(candidate) > 90
                    and not candidate.startswith('{"from') and "/images/" not in candidate):
                return candidate
    raise SystemExit("no summary found for " + slug)


# ------------------------------------------------------------ shared globals
def _category_pairs():
    pairs = []
    for old, new in CATEGORY_LABELS:
        pairs.append(('optionTitles:["%s","%s","%s"]'
                      % tuple(x[0] for x in CATEGORY_LABELS),
                      'optionTitles:["%s","%s","%s"]'
                      % tuple(x[1] for x in CATEGORY_LABELS)))
        pairs.append(('optionTitles":["%s","%s","%s"]'
                      % tuple(x[0] for x in CATEGORY_LABELS),
                      'optionTitles":["%s","%s","%s"]'
                      % tuple(x[1] for x in CATEGORY_LABELS)))
        pairs.append(('"%s","other articles"' % old, '"%s","other articles"' % new))
        pairs.append((">%s<" % old, ">%s<" % new.replace("&", "&amp;")))
        pairs.append((",%s," % old, ",%s," % new.replace("&", "&amp;")))
    return pairs


SHARED = (list(GLOBAL)
          + PROJECT_TAGS
          + PROJECT_COPY
          + journal_pairs()
          + _category_pairs())


# ------------------------------------------------------------------- patches
# Framer's runtime mounts its "Buy this template" badge into
# #__framer-badge-container. The export ships the CSS for it but not the element
# itself, so hydrateRoot() is called with null and throws "Minified React error
# #405" on every page. tools/build.py injects the missing element.
BADGE_CONTAINER = '<div id="__framer-badge-container"></div>'

# The bundled react-dom tries to hydrate the server markup, but the export's
# SSR split-text markup was produced by a different build of the split-text code
# component, so hydration throws (#418/#421/#423) and React falls back to a
# client render anyway. Doing that render directly avoids the hydration errors.
HYDRATE_GUARD = (
    "Mp=kp.hydrateRoot",
    "Mp=function($$el,$$tree,$$opts){if($$el&&$$el.nodeType){"
    "return Ap.createRoot($$el).render($$tree)}"
    "console.warn('[site] no mount container for hydrateRoot; skipped');"
    "return undefined}",
)

PATCHES = {
    "js/react.73opg4pm.mjs": [HYDRATE_GUARD],
}

# rerouter.js rewrites the original Framer URLs to relative paths at runtime, which
# resolves the homepage link to /index. Point them at the canonical clean URLs.
REROUTER_MAP = re.compile(
    r'("https://nudge-folio\.framer\.website[^"]*"):"([^"]*)"')

# The four project detail pages are hand-built static pages, not Framer routes.
# Framer's client router would intercept clicks to them and crash with a fatal
# error, so force a full page load for exactly these links.
STATIC_ROUTES = (
    "/case-study/enterprise-graphrag",
    "/case-study/multi-agent-copilot",
    "/case-study/expertgpt-excel-agent",
    "/case-study/llm-analysis-pipeline",
)
STATIC_NAV = (
    "document.addEventListener('click',function(e){"
    "if(e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.defaultPrevented)return;"
    "var t=e.target&&e.target.closest?e.target.closest('a[href]'):null;"
    "if(!t)return;var u;try{u=new URL(t.getAttribute('href'),location.href)}catch(x){return}"
    "if(u.origin!==location.origin)return;"
    "var ok=%s;"
    "if(!ok)return;e.preventDefault();e.stopPropagation();location.assign(u.pathname);"
    "},true);" % ("[" + ",".join("'%s'" % s for s in STATIC_ROUTES) + "].indexOf(u.pathname)>=0")
)


def _rerouter_link(match):
    target = match.group(2).lstrip("./")
    if target == "blog/index":
        target = "blog"
    return '%s:"/%s"' % (match.group(1), "" if target == "index" else target)


# ------------------------------------------------------------------ applying
def apply(page, html):
    """Apply copy to a generated page."""
    pairs = SCOPED.get(page, []) + SHARED
    html = _sub(html, pairs)
    for old, new in SPLIT.get(page, []):
        html = replace_split(html, old, new)

    title = PAGE_TITLES.get(page)
    if title and title != HOME_TITLE:
        html = html.replace("<title>%s</title>" % HOME_TITLE,
                            "<title>%s</title>" % title, 1)
        html = html.replace('property="og:title" content="%s"' % HOME_TITLE,
                            'property="og:title" content="%s"' % title, 1)
        html = html.replace('name="twitter:title" content="%s"' % HOME_TITLE,
                            'name="twitter:title" content="%s"' % title, 1)
    return html


def apply_bytes(path, data):
    """Apply copy to a JS / JSON / .framercms bundle."""
    page = MODULE_TO_PAGE.get(path)
    pairs = SCOPED.get(page, []) + SCOPED_JS.get(page, []) + SHARED

    if path.endswith(".framercms"):
        return _sub_tlv(data, pairs)

    text = data.decode("utf-8", errors="surrogateescape")
    text = _sub(text, pairs)
    if path.endswith("rerouter.js"):
        text = REROUTER_MAP.sub(_rerouter_link, text)
        text = text.rstrip() + "\n" + STATIC_NAV + "\n"
    for old, new in PATCHES.get(path, []):
        if old not in text:
            raise SystemExit("patch target missing in %s: %r" % (path, old[:60]))
        text = text.replace(old, new, 1)
    return text.encode("utf-8", errors="surrogateescape")


def _sub_tlv(data, pairs):
    """Rewrite the big-endian length-prefixed strings inside a .framercms blob.

    Layout is [type byte 0x0c for string][uint32be length][bytes]; field keys are
    stored the same way without the type byte.
    """
    for pair in pairs:
        for so, sn, nth in _variants(pair):
            ob, nb = so.encode("utf-8"), sn.encode("utf-8")
            if not ob or ob == nb:
                continue
            for typed in (b"\x0c", b""):
                head = typed + len(ob).to_bytes(4, "big")
                tail = typed + len(nb).to_bytes(4, "big")
                pattern = head + ob
                while pattern in data:
                    data = data.replace(pattern, tail + nb, 1)
    return data