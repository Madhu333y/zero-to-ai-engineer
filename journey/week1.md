# Week 1 — FastAPI + Rate Limiting

## What I built

Built a rate limiting system from scratch in FastAPI — four endpoints, each one adding more complexity than the last.

**Endpoint 1 — `/counter`**
Basic counter per username. Allows 3 uses then throws a 429. Used in-memory dictionary to track state. First time using `HTTPException` properly.

**Endpoint 2 — `/premium_limit`**
Same idea but with two tiers — premium users get 7 requests, basic users get 3. Introduced `Field(..., min_length=3)` for input validation. First time using Pydantic `Field`.

**Endpoint 3 — `/warning`**
Added a warning system — when the user is one request away from the limit, the response flags `warning: true`. Had to think carefully about when to trigger the warning vs when to block.

**Endpoint 4 — `/violation`**
Most complex endpoint. Tracks violations — if a user exceeds the limit more than once they get a warning, exceed it again they get suspended permanently. Four pieces of state per user: `uses`, `violation`, `suspended`, `warning`.



---

## What broke

Writing from memory broke me.

I did not copy-paste any of this. I wrote everything from memory, deleted it, and wrote it again. Every single time something was wrong — wrong variable name, forgot to initialise the dictionary, mixed up `uses >= limit` vs `uses > limit`, returned the wrong state.

The violation endpoint especially. The logic for when to suspend vs when to warn took multiple rewrites to get right. I kept reading the wrong variable instead of the updated state.

---

## How I fixed it

Kept writing it again. No shortcuts. When it broke I read the error, traced the variable, fixed it, deleted it, wrote it again from scratch.

The discipline was: understand why it broke before fixing it. Not just change the line until it works.

---

## Real numbers

| Item | Value |
|------|-------|
| Hours spent | 12 |
| GitHub commits | — |
| API cost | ₹0 (not applicable until Month 5) |
| Endpoints built | 4 |
| Times rewrote from memory | multiple |

---

## What I learned

**Limit validation logic is not obvious.** The difference between `uses >= limit` and `uses > limit` changes everything. Off-by-one errors are real and they are silent — the system works, just incorrectly.

**State management in memory is fragile.** Every endpoint uses a dictionary. If the server restarts, all state is gone. This is fine for learning. Not fine for production. Month 6 fixes this with Redis.

**Writing from memory is the real test.** If you can write it from memory, you understood it. If you can't, you only recognised it when you saw it. Recognition is not understanding.

**Pydantic Field validation happens before your function runs.** If `min_length=3` fails, FastAPI returns a 422 automatically. You do not need to check it yourself. That is the point of Pydantic.

**429 is the correct status code for rate limiting.** Not 400. Not 403. 429 — Too Many Requests.

---

## Next week

- HTTP methods — GET vs POST vs PUT vs DELETE, when to use each
- JWT tokens — how they work, how to validate them in FastAPI
- API key authentication — header-based pattern
- Environment variables for secrets — never hardcode keys


