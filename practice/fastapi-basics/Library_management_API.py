from fastapi import FastAPI , HTTPException


app  =  FastAPI()


users = {}
books = {}

DEFAULT_BOOK = {'available': True}

def make_user(user_id):
    return users.setdefault(user_id , {"borrowed": [],"violations": 0})



def make_book(book_id):
    return books.setdefault(book_id, DEFAULT_BOOK.copy() )


@app.post('/book/{book_id}')
def add_books(book_id :str):
    
    
    if book_id in books:
        raise HTTPException(status_code=400,detail="Book already exist")
    make_book(book_id)
    
    
    return {
        "book":book_id,
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
        
        users.setdefault(user_id, {"borrowed": [],"violations": 0})
        
        
    if not books[book_id]['available'] :
        raise HTTPException(status_code=400,detail="Book already borrowed")
    
    
    if len(users[user_id]["borrowed"]) >=  3:
        users[user_id]['violations'] += 1
        
        
        raise HTTPException(status_code=429 , detail="limit reached")
    
    users[user_id]["borrowed"].append(book_id)
    
    books[book_id]['available'] = False
    
    
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


    if user_id in users and book_id in books:
        
        if book_id not in users[user_id]["borrowed"]:
            raise HTTPException(
            status_code=400,
            detail="User did not borrow this book"
        )
        
        users[user_id]["borrowed"].remove(book_id)
        
        books[book_id]["available"] = True
        

    
    return {
        "message": "Book Returned"
    }