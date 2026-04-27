from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI(title="Bookstore API")

# In-memory DB
books = []

# Book Model
class Book(BaseModel):
    id: str = None
    title: str
    author: str
    price: float

# Create Book
@app.post("/books", response_model=Book)
def create_book(book: Book):
    book.id = str(uuid4())
    books.append(book)
    return book

# Get All Books
@app.get("/books", response_model=List[Book])
def get_books():
    return books

# Get Book by ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: str):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Update Book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: str, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_book.id = book_id
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete Book
@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")