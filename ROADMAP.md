# The Master Roadmap

## Foundation → AI Application Engineer
**8 Months · Production Edition · March 2026**

---

## Core Philosophy

> AI Application Engineering = Backend Engineering + LLM Control + Production Reliability + Cost Efficiency + Observability

Goal: Build reliable, observable, cost-aware AI systems that survive real users — not just demos.

---

## 8-Month Overview

| Month | Phase | Focus | You Can Do After |
|-------|-------|-------|-----------------|
| 1 | Foundation | Python runtime + terminal | Understand exactly how code runs and fails |
| 2 | Foundation | FastAPI + HTTP + Auth | Build and expose a secure backend API |
| 3 | Foundation | Model inference basics | Run AI models safely inside a backend |
| 4 | Foundation | Async + concurrency | Backend survives real traffic load |
| 5 | AI Systems | LLM APIs + prompt engineering | Wire real AI models into your backend |
| 6 | AI Systems | Docker + cloud + CI/CD + observability | Ship anywhere, see everything |
| 7 | AI Systems | RAG + vector DB + evaluation | Build AI that reasons over real data |
| 8 | AI Systems | Agents + tools + output validation | Build AI that takes real actions |

---

## Phase 1 — Engineering Foundation (Months 1–4)

*No LLMs. No shortcuts. Understanding how systems actually work.*

---

### Month 1 — Python Runtime & Engineering Basics

**Goal:** Understand exactly how backend code executes and fails.

**Learn:**
- Terminal workflow — Linux/CLI mindset, daily usage
- Python fundamentals — backend focused
- Virtual environments — venv, why they exist
- Dependency management — pip, requirements.txt, version pinning
- Program execution lifecycle — how Python starts, runs, crashes
- Reading stack traces — practice daily
- Logging basics — Python logging module
- Git and GitHub — commit, push, branches

**Build:**
- Terminal-only programs
- Scripts that follow Input → Process → Output
- Intentionally break every script then fix it
- Push every project to GitHub from day one

**Rule:** No frameworks. No cloud. No AI. Understand how Python runs first.

---

### Month 2 — Backend APIs — FastAPI

**Goal:** Expose backend logic as a clean, secure, structured API.

**Learn — HTTP Fundamentals:**
- HTTP methods — GET, POST, PUT, DELETE
- Headers, status codes, request/response lifecycle

**Learn — FastAPI:**
- Routing, request/response models, dependency injection
- Input validation with Pydantic

**Learn — Security Basics:**
- API key authentication
- JWT tokens
- Input sanitization
- Prompt injection awareness
- Rate limiting basics
- Environment variables for secrets

**Learn — Database:**
- Minimal SQL — CREATE TABLE, INSERT, SELECT, UPDATE
- SQLite first, then PostgreSQL
- SQLAlchemy ORM basics

**Build:**
- Secure backend with /predict, /health, /status endpoints
- API key + JWT authentication on every endpoint
- Every request logged to SQLite

---

### Month 3 — Model Inference Basics

**Goal:** Run AI models safely inside a backend.

**Learn:**
- Inference vs training distinction
- Load model once at startup — never per request
- CPU vs GPU inference — conceptual understanding
- Token counting — every token costs money
- Cost per query calculation
- Model tier decisions
- Monthly cost projections
- Cost logging per endpoint

**Build:**
- AI inference backend
- Measure inference latency and memory usage
- Add cost tracking to every LLM call

---

### Month 4 — Async, Concurrency & Performance

**Goal:** Backend survives multiple users without collapsing.

**Learn:**
- async/await — what it actually does at runtime
- The event loop
- Blocking vs non-blocking operations
- Rate limiting with slowapi
- Exponential backoff with tenacity
- Redis — persistent shared cache
- Request cache — prompt hash → cached answer
- pytest and httpx for testing

**Build:**
- All FastAPI endpoints converted to async
- Redis caching for LLM responses
- Rate limiting and backoff on all LLM calls
- Load test with locust — 100 concurrent users

---

## Phase 2 — AI Application Systems (Months 5–8)

*Foundation is solid. Now building real AI systems.*

---

### Month 5 — LLM APIs + Prompt Engineering + Caching

**Goal:** Wire real AI models into the backend and control their behavior precisely.

**Learn:**
- OpenAI / Claude / Gemini API patterns
- Token limits and context windows
- Temperature and parameter control
- Streaming responses
- System prompts and few-shot examples
- Prompt injection defense
- LiteLLM — one interface for all providers
- Provider fallback strategy

**Build:**
- Full AI-powered API with retry + backoff + cache + streaming + cost logging

---

### Month 6 — Docker + Cloud + CI/CD + Observability

**Goal:** System runs anywhere and you can see exactly what is happening inside it.

**Learn:**
- Docker — containers, Dockerfiles, multi-stage builds
- Background jobs — Redis + Celery/RQ
- Cloud deployment — Fly.io / Railway / Render
- GitHub Actions CI/CD pipeline
- Langfuse or Arize Phoenix for observability
- Traces, token usage, latencies, costs dashboard

**Build:**
- Fully Dockerized AI backend
- Deployed to cloud with HTTPS
- GitHub Actions CI/CD with rollback
- All LLM calls traced in Langfuse

---

### Month 7 — RAG + Vector DB + ML Basics + Evaluation

**Goal:** Build AI that reasons over real data and measure whether it works.

**Learn — ML Basics (2 weeks):**
- What embeddings actually are
- Cosine similarity
- Supervised vs unsupervised — conceptual
- Fine-tuning vs RAG — when to use which
- Evaluation metrics — precision, recall, F1

**Learn — RAG:**
- Documents → chunking → embeddings → vector store → retrieve → augment → generate
- Chunking strategies — fixed, semantic, recursive
- Qdrant or Chroma vector databases

**Learn — Evaluation:**
- LLM-as-judge
- Ragas library — context precision, recall, faithfulness
- Iterate: bad score → fix → re-eval

**Build:**
- Document QA API — /upload and /query endpoints
- Eval script with batch metrics

---

### Month 8 — Agents + Tools + Structured Outputs

**Goal:** Build AI that takes actions, completes multi-step tasks, returns validated outputs.

**Learn:**
- Function calling at the API level
- ReAct-style agent loop — think → tool → execute → observe → repeat
- Max iterations guard
- Pydantic schemas for output validation
- Instructor library
- Retry logic on schema mismatch

**Build:**
- Agent with tools: search_documents(), get_current_date(), summarize_text(), save_result()
- Every tool call logged
- Full tracing in Langfuse
- All outputs validated against Pydantic schema

---

## Final Stack

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

## Weekly Non-Negotiable Habit

Every Friday for all 8 months:

- Push all code to GitHub
- Write a clear README for every project
- Post one thing on LinkedIn
- Update progress bars in README.md

> By Month 8 you will have 32 LinkedIn posts and a GitHub showing 8 months of consistent real work.

---


*The roadmap is not the destination. It is the spine that makes every destination reachable.*

**Month 1. Terminal. Python. Tomorrow morning.**
