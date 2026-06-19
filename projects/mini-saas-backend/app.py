from fastapi import FastAPI , HTTPException

app  =  FastAPI()

users = {}
logs =  []
DEFAULT_O =  {'uses':0,'premium':True,'violation':0,'suspended':False,'admin':False,'lifetime':0}
LIMIT =  {'premium':6,'normal':3}
Lifetime_limit = 20

def log_event(user_id,result,remaining = None):
    
    logs.append({
        'user_id':user_id,
        'Result':result,
        'remaining':remaining
    })
    
    
def make_state(user_id):
    return users.setdefault(user_id , DEFAULT_O.copy())


def rules(user_id,state):
    
    uses = state.get('uses', 0)
    
    if state['suspended'] :
        log_event(
            user_id,
            'suspended',
            0
            
        )
        
        raise HTTPException(status_code=403, detail="suspended")
    
    limit =  LIMIT['premium'] if state['premium'] else LIMIT['normal']
    
    if state['uses'] >= limit :
        state['violation'] += 1
        
        if state['violation'] >= 2:
            state['suspended'] = True
        
        log_event(
            user_id,
            'blocked',
            0
            
        )
        
        raise HTTPException(status_code=429, detail=" Limit reached")
    
    if state['lifetime'] >=  Lifetime_limit:
        
        log_event(
            user_id,
            'lifetime limit reached',
            0
        )
        raise HTTPException(status_code=429, detail="Lifetime limit reached")
    
def increment(state):
    
    state['uses'] += 1
    state['lifetime'] += 1
    
    if state['lifetime'] >= 10:
        state['premium'] = True


@app.get('/request/{user_id}')
def first_one(user_id:str):
    
    if not user_id.strip():
        raise HTTPException(
            status_code=400,
            detail='Empty user id '
        )
    
    state =  make_state(user_id)
    
    if state['admin']:
        
        state['uses'] +=1
        
        log_event(
        user_id,
        'admin_allowed',
        'unlimited'
        )
        
        return{
            'user': "Admin",
            'uses': state['uses']
            
        }
    rules(user_id,state)
    
    increment(state)
    
    limit =  LIMIT['premium'] if state['premium'] else LIMIT['normal']
        
    remaining =  limit - state['uses']
    log_event(
        user_id,
        'allowed',
        remaining
        
    )
    
    return{
        'user_id':user_id,
        'remaining':remaining,
        'violation':state['violation'],
        
    }

    
@app.post('/reset/{user_id}')
def reset(user_id : str):
    if user_id not in users:
        
        raise HTTPException(status_code=404,detail="user not exist")
    
    users[user_id]['uses'] = 0
    users[user_id]['violation'] = 0
    
    return {
        'user': "reset daily state complete"
    }
    
@app.get('/logs')
def get_logs():
    return logs