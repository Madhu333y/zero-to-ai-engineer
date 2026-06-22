from fastapi import FastAPI,HTTPException

app =  FastAPI()

users =  {}
DEFAULT_LIST = {'uses':0, 'premium':False, 'violations':0,'suspended':0,'admin': False,'lifetime':0}
LIMIT = {'premium':5, 'normal':4}
logs = []
lifetime_limit =  22

def log_event(user_id, result , remaining = None) :
    logs.append({
        'user' :     user_id,
        'result':    result,
        'remaining': remaining
        
    })
    
def make_state(user_id):
    return  users.setdefault(user_id, DEFAULT_LIST.copy() )

def rules(user_id,state):
    
    if state['suspended']:
        
        log_event(
            user_id,
            'suspended',
            0
        )
        
        raise HTTPException(status_code=402,detail='suspended')


    limit =  LIMIT['premium'] if state['premium'] else LIMIT['normal']
    
    if state['uses'] >=  limit :
        state['violations'] += 1
        
        if state['violations'] >= 2:
            state['suspended'] = True
            
            
            
        log_event(
            user_id,
            'Blocked',
            0
        )
        raise HTTPException(status_code=429,detail="Limit reached")
    
    
def increment(state,user_id):
    
    state['uses'] += 1
    state['lifetime'] += 1
    
    if state['lifetime'] >=  lifetime_limit:
        
        log_event(
            user_id,
            'lifetime blocked',
            0
        )
        
        raise HTTPException(status_code=402,detail="Lifetime limit blocked")
    
@app.get('/request/{user_id}')
def project_1(user_id:str):
    
    state = make_state(user_id)
    
    rules(user_id,state)
    
    increment(state,user_id)
    
    limit =  LIMIT['premium'] if state['premium'] else LIMIT['normal']
    
    remaining =  limit -  state['uses']
    
    
    log_event(
        user_id,
        'sucsess',
        remaining
    )
    
    return {
        'user_id': user_id,
        'remaining': remaining,
        'violations': state['violations']
    }

@app.post('/reset{user_id}')
def make_reset(user_id : str):
    
    if user_id not in users:
        
        log_event(
            user_id,
            "Not found",
            0
        )
        
        raise HTTPException(status_code=404,detail='Not found')
    
    users[user_id]['uses'] = 0
    users[user_id]['violations'] = 0
    
    
    return {
        'reset': 'reset successful'
    }
    
@app.get('/logs')
def get_logs():
    return logs
