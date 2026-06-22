from fastapi import FastAPI , HTTPException
app =  FastAPI()

logs = []
users = {}
LIMIT = {'premium':6,'normal':5}
DEFAULT_LIST = {'uses':0,'premium':False,'violations':0,'suspended':False,'admin':False,'lifetime':0,'system_toatal':0}
lifetime_limit =  15
system =  {'system_total':0}
GLOBAL_LIFETIME = 20


def log_event(user_id,result,remaining=None):
    
    logs.append({
        "user_id":user_id,
        "Result": result,
        "remaining":remaining,
        
    })
    
def make_state(user_id):
    return users.setdefault(user_id, DEFAULT_LIST.copy())

def rules(user_id,state):
    
    if state['suspended']:
        
        log_event(
            user_id,
            "suspended",
            0
        )
        raise HTTPException(status_code=403,detail="Suspended")
        
    limit =  LIMIT['premium'] if state['premium'] else LIMIT['normal']
    
    if system['system_total'] >= GLOBAL_LIFETIME:
        
        log_event(
            user_id,
            'Global limit reached',
            0
        )
        
        raise HTTPException(status_code=503, detail='System capacity reached')

    
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
    
    if state['lifetime'] >= lifetime_limit:
        
        log_event(
            user_id,
            "Lifetime limit reached",
            0
        )
        
        
        raise HTTPException(status_code=429,detail="Lifetime limit reached")
        
    
def increment(state,user_id):
    
    state['uses'] += 1
    state['lifetime'] += 1 
    
    system['system_total']  += 1

    
    if state['lifetime'] >= 10:
        state['premium'] =  True
    

    
@app.get('/request/{user_id}')
def project_1(user_id : str ):
    
    
    state =  make_state(user_id)
    
    if not user_id.strip():
        raise HTTPException(
            status_code=400,
            detail='Empty user id '
        )
    
    if state['admin']:
        
        state['uses'] += 1
        
        return {
            'user': "Admin",
            'uses': state['uses']
        }
        
    rules(user_id,state)
    increment(state,user_id)
    
    limit =  LIMIT['premium'] if state['premium'] else LIMIT['normal']
    
    remaining =  limit -  state['uses']
    
    log_event(
        user_id,
        "Success",
        remaining
    )
    
    return {
        'user': user_id,
        'reamining': remaining,
        'life_time_uses' : state['lifetime'],
        'Global_limit' : system['system_total']
    }
    
    
@app.post('/reset')
def make_reset(user_id:str):
    if user_id not in users:
        
        log_event(
            user_id,
            "Not found",
            0
        )
        
        raise HTTPException(status_code=404, detail='User not found')
    
    users[user_id]['uses'] = 0
    users[user_id]['violations'] =  0
    
    return {
        user_id : "reset successful"
        
    }
    
    



@app.post('/logs')
def get_logs():
    return logs

@app.get("/users")
def get_users():
    return users


@app.post('/premium/user_id')
def make_premium(user_id:str):
    
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    
    users[user_id]['premium'] = True
    
    return{
        user_id : "Is premium member"
    }

# for exixting user_id make premium 

@app.post('/premium/{user_id}')
def make_premium(user_id: str):

    state = make_state(user_id)
    state['premium'] = True

    return {
        user_id: "Is premium member"
    }
    
# to make new user_id and existing user_id to make premium

@app.post('/admin/{user_id}')
def make_admin(user_id: str):
    
    state =  make_state(user_id)  # this line i have understand how this one is working how reacalling actually working
    state['admin'] =  True
    
    return{
        user_id : "is now Admin"
    }
    
@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    
    
        
    if user_id not in users:
        
        raise HTTPException(status_code=404 , detail="user not exist ")
        
    del  users[user_id]
        
    return {
            user_id : "User is deleted"
        }