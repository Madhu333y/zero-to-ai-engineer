from fastapi import FastAPI, HTTPException
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
    
