from fastapi import FastAPI , HTTPException
from pydantic import BaseModel, Field ,ConfigDict, EmailStr

app =  FastAPI()


users = {}


def register_user(user):
        users[user.username] = {
        "password": user.password,
        "email": user.mail,
        "logged_in": False
    }

class Register(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    
    username : str =  Field(...,min_length = 5, max_length = 15 , pattern="^[a-zA-Z0-9_-]+$", description="Alphanumeric, 5-15 characters")
    password : str = Field(..., min_length = 8, max_length = 12)
    mail : EmailStr 
    
    
@app.post('/register')
def register_(register : Register):
    
    if register.username in users:
        raise HTTPException(status_code=400, detail="user already exists")
    
    register_user(register)
    
    
    return{
        "user": register.username,
        "status" : "added"
    }
    

class Login(BaseModel):
    username: str
    password: str
    
@app.post('/login')
def login_user(login : Login):
    
    if login.username not in users:
        
        raise HTTPException(status_code=404 , detail="User does not exist")
    
    
        
    if login.password != users[login.username]["password"]:
        
        raise HTTPException(status_code=401, detail="Password doesn't match")
        
    users[login.username]["logged_in"] = True
        
    return {login.username : users[login.username]["logged_in"]  }
    

        
@app.get('/profile/{username}')
def get_profile(username):
    
    if username not in users:
        raise HTTPException(
            status_code= 404 ,
            detail= "User not in data"
        )
        
    return {
        "username":username,
        "email": users[username]["email"],
        "logged_in": users[username]["logged_in"]
    }
class PasswordChange(BaseModel):
    username : str
    old_password : str
    new_password : str
    
@app.post('/change-password')
def change_pass(password_change : PasswordChange):
    
    if password_change.username not in users :
        
        raise HTTPException(status_code=404, detail="User does not exist")
    
    
    
    if password_change.Old != users[password_change.username]["password"]:
        
        raise HTTPException(status_code=401, detail="Password doesn't match")
    
    
        
    if password_change.New == password_change.Old :
        raise HTTPException(status_code=400 ,detail= "Password should not match")
    
    users[password_change.username]["password"] = password_change.New
        
        
    return {
        "username" : password_change.username,
        "New_password_change": "Success"
    }
    
        
        
        
@app.delete('/delete-user/{username}')
def delete_user(username):
    
    if username not in users:
        raise HTTPException(status_code=404 , detail="User does not exist")
    
    del users[username]
    
    return {username : "successfully deleted"}