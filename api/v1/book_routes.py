from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.book import BookCreate, BookResponse
from services import book_service
from models import Book

router = APIRouter()

@router.post("/books", response_model=BookResponse)
def create(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book)

@router.get("/books", response_model=list[BookResponse])
def get_all(db: Session = Depends(get_db)):
    return book_service.list_books(db)

@router.get("/books/{book_id}", response_model=BookResponse)
def get_one(book_id: str, db: Session = Depends(get_db)):
    book = book_service.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/books/{book_id}")
def delete(book_id: str, db: Session = Depends(get_db)):
    book = book_service.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Deleted"}

@router.post("/borrow")
def borrow(book_id: str, user_id: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book or book.available_copies <= 0:
        raise HTTPException(400, "Book not available")

    loan = Loan(
        user_id=user_id,
        book_id=book_id,
        due_date=datetime.utcnow() + timedelta(days=14)
    )

    book.available_copies -= 1

    db.add(loan)
    db.commit()

    return {"message": "Book borrowed"}

@router.post("/return/{loan_id}")
def return_book(loan_id: str, db: Session = Depends(get_db)):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()

    if not loan or loan.returned_at:
        raise HTTPException(400, "Invalid loan")

    loan.returned_at = datetime.utcnow()

    book = db.query(Book).filter(Book.id == loan.book_id).first()
    book.available_copies += 1

    db.commit()

    return {"message": "Book returned"}



