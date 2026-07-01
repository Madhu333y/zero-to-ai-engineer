from fastapi import FastAPI , HTTPException
from pydantic import BaseModel, Field ,ConfigDict, field_validator

app  =  FastAPI()


users = {}
books = {}



def make_user(user_id):
    return users.setdefault(user_id , {"borrowed": [],"violations": 0})



def make_book(book):
    books[book.id] = {
    "id": book.id,
    "title": book.title,
    "author": book.author,
    "available": True,
    "borrowed_by": None
}



class Book(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    
    id : str =  Field(..., min_length=1)
    title : str =  Field(..., min_length = 2, max_length = 100)
    author : str =  Field(..., min_length = 2, max_length = 50)
    
    @field_validator("id", "title", "author")
    @classmethod
    def validate_not_blank(cls, value):
        if not value.strip():
            raise ValueError("Field cannot be empty or only spaces")
        return value
    
@app.post('/book')
def add_books(book_id :Book):
    
    
    if book_id.id in books:
        raise HTTPException(status_code=400,detail="Book already exist")
    make_book(book_id)
    
    
    return {
        "book":book_id.id,
        "status": "added"
    }
    
@app.get('/books')
def get_books():
    return books



@app.get('/borrow/{user_id}/{book_id}')
def borrow(user_id,book_id):
    
    if book_id not in books:
        raise HTTPException(status_code=404,detail="Book not found")
    
    if user_id not in users:
        
        make_user(user_id)
        
        
    if not books[book_id]['available'] :
        raise HTTPException(status_code=400,detail="Book already borrowed")
    
    
    if len(users[user_id]["borrowed"]) >=  3:
        users[user_id]['violations'] += 1
        
        
        raise HTTPException(status_code=429 , detail="limit reached")
    
    users[user_id]["borrowed"].append(book_id)
    books[book_id]['available'] = False
    books[book_id]["borrowed_by"] = user_id
    
    return {
    "user": user_id,
    "book": book_id,
    "status": "borrowed"
}
    
@app.post('/return/{user_id}/{book_id}')
def return_books(user_id,book_id):
    
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )


    
        
    if book_id not in users[user_id]["borrowed"]:
        raise HTTPException(
        status_code=400,
        detail="User did not borrow this book"
    )
    
    users[user_id]["borrowed"].remove(book_id)
    books[book_id]["available"] = True
    books[book_id]["borrowed_by"] = None


    return {
    "message": "Book Returned"
    }

@app.get("/users")
def get_users():
    return users