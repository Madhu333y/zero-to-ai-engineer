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

Full code: [`month-02-fastapi-http-auth/`](../month-02-fastapi-http-auth/)

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


## Code
```python
# from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import logging

app = FastAPI()

logger = logging.getLogger(__name__)

# basic counter

locker = {}

class Counter(BaseModel):
    username : str
    
    
@app.post("/counter")
def basic_counter(counter:Counter):
    logger.info("Processing")
    
    if counter.username not in locker:
        locker[counter.username] = 0
        

    state = locker[counter.username]
    basic_uses = state
    
    if basic_uses > 3:
        logger.error("Limit crossed")
        raise HTTPException(status_code=429,detail="Limit crossed")
    
    locker[counter.username] += 1
    
    return{
        "usename":counter.username,
        "remain": basic_uses
    }
    

track = {}

class Limitp(BaseModel):
    username: str = Field(...,min_length=3)
    premium: bool = False
    
@app.post("/premium_limit")
def premium_limit(limit:Limitp):
    logger.info("processing")
    
    if limit.username not in track:
        track[limit.username] = 0
        
    state = track[limit.username]
    uses = state
    
    limi = 7 if limit.premium else 3
    
    if uses >= limi :
        logger.error("Limit crossed")
        raise HTTPException(status_code=429, detail="limit crossed")
    
    track[limit.username] += 1
    
    return {
        "username":limit.username,
        "uses": uses
    }

new_room = {}

class Warning(BaseModel):
    username: str = Field(...,min_length=4)
    premium : bool = False
    
    
@app.post("/warning")
def thresholds(warning: Warning):
    logger.info("processsing")
    
    if warning.username not in new_room:
        new_room[warning.username] = {
            "uses" : 0,
            "warning": False
        }
        
    state = new_room[warning.username]
    Warning_req = state["warning"]
    uses = state['uses']
    
    limit = 7 if warning.premium else 3
    
    if uses >= limit:
        logger.error("limit crossed")
        raise HTTPException(status_code=429,detail="limit crossed")
    
    if uses == limit - 1:
        Warning_req = True
        
    state['uses'] += 1
    
    return {
        "username" : warning.username,
        "warning" : Warning_req,
        "uses": uses
    }
    
    
room = {}

class Suspended(BaseModel):
    username: str
    premium : bool = False
    
@app.post("/violation")
def violation(suspended: Suspended):
    logger.info("processing")
    
    
    
    if suspended.username not in room :
        room[suspended.username] = {
            "uses" : 0,
            "violation" :0,
            "suspended_re": False,
            "warning_req": False
        }
        
    state =  room[suspended.username]
    
    violation_req = state["violation"]
    uses = state["uses"]
    suspended_req = state["suspended_re"]
    warning_req = state["warning_req"]
    
    limit = 7 if suspended.premium else 3
    
    if suspended_req == True:
                logger.error("user suspended")
                raise HTTPException(status_code=429, detail="user Suspended")
        
    if uses > limit :
        state["violation"] += 1
        violation_req = state["violation"]
        
        if violation_req >= 2:
            state["suspended_re"] = True
            suspended_req  = state["suspended_re"] 
            
        
    if violation_req == 1 :
        state["warning_req"] = True
        warning_req = state["warning_req"]
        
    state["uses"] += 1
    
    return {
        "username" : suspended.username,
        "uses" : uses,
        "violation": violation_req,
        "warning": warning_req
        
    }
    
```
