# Week 01 — FastAPI Basics + Rate Limiting

## 🔗 Code

practice/fastapi-basics/rate-limiting-basic.py

## 🧠 System Overview

In-memory rate limiting using per-user state tracking via Python dictionaries.

---

## What I built

Built a rate limiting system from scratch in FastAPI — four endpoints, each increasing in complexity.

**Endpoint 1 — `/counter`**
Basic counter per username. Allows 3 uses, then returns HTTP 429.
Used an in-memory dictionary to track state. First proper use of `HTTPException`.

**Endpoint 2 — `/premium_limit`**
Introduced user tiers — premium users get 7 requests, basic users get 3.
Used Pydantic `Field(..., min_length=3)` for input validation.

**Endpoint 3 — `/warning`**
Added a warning system — when a user is one request away from the limit, the response includes `warning: true`.
Required careful handling of threshold conditions.

**Endpoint 4 — `/violation`**
Tracks repeated violations.
If a user exceeds the limit multiple times:

* First → warning
* Second → permanent suspension

State tracked per user:

* `uses`
* `violations`
* `warning`
* `suspended`

---

## What broke

Writing this from memory exposed gaps in my understanding.

Common issues:

* Incorrect variable initialization
* Mixing up conditions (`uses >= limit` vs `uses > limit`)
* Reading stale state instead of updated values

The violation logic required multiple rewrites to correctly handle state transitions.

---

## How I fixed it

Focused on understanding failures instead of patching them.

Process:

* Read the error carefully
* Trace variable state step-by-step
* Fix the root cause
* Rewrite the logic again from scratch

This helped clarify where my understanding was incomplete.

---

## Real numbers

| Item            | Value                             |
| --------------- | --------------------------------- |
| Hours spent     | 12                                |
| Endpoints built | 4                                 |
| Bugs faced      | Off-by-one errors, state mismatch |
| API cost        | ₹0 (not applicable yet)           |

---

## What I learned

**Off-by-one errors are subtle but critical.**
The difference between `uses >= limit` and `uses > limit` changes system behavior silently.

**State management is fragile in memory.**
All state is lost on restart. Acceptable for learning, not for production (will move to Redis later).

**Validation happens before execution.**
Pydantic enforces constraints before the function runs — no need for manual checks.

**Correct status codes matter.**
429 (Too Many Requests) is the proper response for rate limiting.

**Understanding > memorization.**
Being able to trace, explain, and modify logic is more important than recalling code from memory.

---

## Next week

* HTTP methods — GET vs POST vs PUT vs DELETE
* JWT authentication — structure and validation
* API key authentication — header-based pattern
* Environment variables for secrets
