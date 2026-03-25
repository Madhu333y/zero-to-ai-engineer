# ⚡ Zero to AI Engineer

> 8 months journey to building production-ready AI systems — built in public.

![Status](https://img.shields.io/badge/status-in%20progress-1D9E75?style=flat-square)
![Month](https://img.shields.io/badge/current-month%202-185FA5?style=flat-square)
![Journey](https://img.shields.io/badge/journey-India%20→%20World-EF9F27?style=flat-square)

---

## ⚡ Quick Overview

- 📅 Month: 02 (FastAPI + Backend Systems)
- 🚀 Current build: Rate limiting system
- 🎯 Goal: AI Backend Engineer 
- 🔁 Weekly system: Build → Break → Fix → Document

---

## What this is

This repository documents my journey of becoming an AI backend engineer by building real systems in public.

I am building myself into an engineer — one month at a time.

Completely in public.

Every mistake. Every fix. Every cost number. Every week of progress. Nothing polished. Nothing hidden.

The goal: complete an 8-month production AI engineering roadmap and document every single step so honestly that the next person who finds this repository has everything they need to follow the same path.

**Philosophy:**
> AI Application Engineering = Backend Engineering + LLM Control + Production Reliability + Cost Efficiency + Observability
>
> *Goal: Build reliable, observable, cost-aware AI systems that survive real users — not just demos.*

---

## The 8-Month Roadmap

### Phase 1 — Engineering Foundation (Months 1–4)
*No LLMs. No shortcuts. Understanding how systems actually work.*

| Month | Focus | Key Outcome |
|-------|-------|-------------|
| 01 | Python runtime + terminal | Understand exactly how code runs and fails |
| 02 | FastAPI + HTTP + Auth + Security | Build and expose a secure backend API |
| 03 | Model inference + cost modeling | Run AI models safely inside a backend |
| 04 | Async + concurrency + caching | Backend survives real traffic load |

### Phase 2 — AI Application Systems (Months 5–8)
*Foundation is solid. Now building real AI systems.*

| Month | Focus | Key Outcome |
|-------|-------|-------------|
| 05 | LLM APIs + prompt engineering + caching | Wire real AI models into the backend |
| 06 | Docker + cloud + CI/CD + observability | Ship anywhere, see everything |
| 07 | RAG + vector DB + ML basics + evaluation | Build AI that reasons over real data |
| 08 | Agents + tools + output validation | Build AI that takes real actions |

---

## Current Progress

```
Month 01 — Python Foundation          ██████████  complete ✓
Month 02 — FastAPI + Security         ██░░░░░░░░ In progress
Month 03 — Model Inference            ░░░░░░░░░░  not started
Month 04 — Async + Concurrency        ░░░░░░░░░░  not started
Month 05 — LLM APIs                   ░░░░░░░░░░  not started
Month 06 — Docker + Cloud             ░░░░░░░░░░  not started
Month 07 — RAG + Vector DB            ░░░░░░░░░░  not started
Month 08 — Agents + Tools             ░░░░░░░░░░  not started 
```

*This bar updates every Friday.*

---

## 🚀 Current Build

**FastAPI Rate Limiting System**

- Per-user request limiting
- Tier-based access (basic vs premium)
- Warning + violation tracking
- Correct HTTP 429 handling
- Built 4 endpoints with increasing complexity

📂 Code:
practice/fastapi-basics/rate-limiting-basic.py

📄 Journey:
journey/month-02/week-01.md
journey/month-02/week-01.md

---

## 📂 Repository Structure

```
zero-to-ai-engineer/
│
├── journey/                            ← weekly build logs (updated every Friday)
│   ├── month-01/
│   │   ├── README.md                   ← month summary + project link
│   │   ├── week-01.md
│   │   ├── week-02.md
│   │   ├── week-03.md
│   │   └── week-04.md
│   │
│   ├── month-02/
│   │   ├── README.md
│   │   ├── week-01.md
│   │   └── week-02.md
│   │
│   ├── month-03/
│   ├── month-04/
│   ├── month-05/
│   ├── month-06/
│   ├── month-07/
│   └── month-08/
│
├── lessons/                           ← hard lessons, saved for everyone
│   ├── production-mistakes.md         ← every mistake + exact fix
│   ├── cost-management-reality.md     ← real API cost numbers
│   ├── debugging-guide.md             ← how to debug AI systems
│   └── what-youtube-never-tells-you.md
│
├── practice/
│   └── fastapi-basics/                # raw learning code (experiments)
│       └── rate-limiting-basic.py
│
├── projects/                          ← links to all 8 monthly builds
│   └── README.md
│
├── resources/                         ← curated tools and data
│   ├── real-cost-data.md              ← actual token costs from real projects
│   ├── job-market-analysis.md         ← real job postings analyzed
│   └── tools-i-actually-use.md        ← not generic lists
│
├── CONTRIBUTING.md                    ← how to follow along or contribute
├── ROADMAP.md                         ← the complete 8-month plan
└── README.md                          ← you are here
```

---

## Weekly Build Log Format

Every Friday I update the relevant `week-XX.md` file with:

```markdown
## Week X — [Month Name]

### What I built
[description of the project or feature]

### What broke
[honest account of what failed]

### How I fixed it
[exact solution]

### Real numbers
- Lines of code: 
- Hours spent: 
- API cost this week: ₹
- GitHub commits: 

### What I learned
[3 to 5 genuine insights]

### Next week
[what month X week Y looks like]

### LinkedIn post
[link to this week's post]
```

No polishing. No making it look easier than it was.

---

## The Final Architecture (What Month 8 Produces)

```
Client Request
      ↓
FastAPI (authenticated + rate-limited + async)
      ↓
Input Validation (Pydantic)
      ↓
Auth Layer (API key / JWT check)
      ↓
Async Router
      ↓
┌─────────────┬──────────────┬─────────────┐
│  LLM Calls  │ RAG Pipeline │ Agent Loop  │
│  (streamed  │              │             │
│  +cached    │              │             │
│  +retried)  │              │             │
└─────────────┴──────────────┴─────────────┘
      ↓
Output Validation (Instructor + Pydantic)
      ↓
Redis (cache + job queue)
      ↓
Workers (Celery / RQ)
      ↓
Vector DB (Qdrant / Chroma)
      ↓
Database Logging (token cost + tool calls + latency)
      ↓
Observability (Langfuse — traces + eval scores)
      ↓
Docker + GitHub Actions CI/CD + Cloud Deploy
```

*This is not a tutorial project. This is a production-grade AI system.*

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python |
| API Framework | FastAPI + Pydantic |
| Database | SQLite → PostgreSQL |
| Cache + Queue | Redis + Celery |
| Containers | Docker |
| Cloud | Fly.io / Railway |
| CI/CD | GitHub Actions |
| LLM APIs | OpenAI / Claude / Gemini |
| Vector DB | Qdrant / Chroma |
| Observability | Langfuse |
| Evaluation | Ragas + LLM-as-judge |
| Output Validation | Instructor + Pydantic |
| Reliability | tenacity + slowapi |

---

## Real Numbers (Updated Monthly)

| Metric | Value |
|--------|-------|
| Total API spend so far | ₹0 |
| Total GitHub commits | 20 |
| LinkedIn followers gained | 2 |
| First Upwork client | not yet |
| Projects shipped | 0 of 8 |

*These numbers are real. No rounding up. No hiding bad weeks.*

---

## Why This Is Different From Every Other AI Repository

Most AI repositories show you the finished, working version.

This one shows you:
- The broken version that failed first
- The 3am debug session that fixed it
- The exact cost of running it at 100 users
- The week where motivation dropped and I pushed anyway
- The honest evaluation scores — not just the good ones

**Because the journey is the learning. And the learning is the point.**

---

## Follow the Journey

**LinkedIn:** https://www.linkedin.com/in/madhusudan-builds
*Every Friday — what I built, what broke, what I learned.*

**The rule I follow:**
> Every Friday: push code to GitHub + post one thing on LinkedIn.
> Do this from Week 1, not Month 8.

---

## The Non-Negotiable Weekly Habit

```
Every Friday — without exception:
  □ Push all code to GitHub
  □ Update this week's journey log
  □ Post one thing on LinkedIn with GitHub link
  □ Document what you built in plain English

By Month 8:
  → 32 LinkedIn posts
  → 8 complete projects
  → One of the most honest AI engineering 
    portfolios on GitHub
```

---

## What You Can Build After 8 Months

- AI knowledge bases and internal document search systems
- Document intelligence APIs — upload, analyze, extract structured data
- Research and analyst agent systems
- Autonomous workflow automation
- Any AI application a real business will pay for

> *These are real production products. Not demos. Not tutorials. Products people pay for.*

---


## If You Want to Follow This Path

This repository is public because the path should be public.

If you are starting a similar journey:

1. Fork this repository
2. Replace my progress with yours
3. Commit every week without fail
4. Post every Friday on LinkedIn
5. Tag me — I will follow your journey too

The more engineers who take this path seriously, the stronger the community becomes.

---

## The Last Line

> The roadmap is not the destination.
> It is the spine that makes every destination reachable.

*Build. Break. Fix. Repeat.*

---

<div align="center">
  <sub>Built in public from Nanded , India · Started February 2026</sub>
</div>
