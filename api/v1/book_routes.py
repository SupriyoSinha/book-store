from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from models.loans import Loan

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

    if not book:
        raise HTTPException(400, "Book not available")

    loan = Loan(
        user_id=user_id,
        book_id=book_id,
        due_date = datetime.utcnow() + timedelta(days=14)
    )

    book.available_copies -= 1

    db.add(loan)
    db.commit()

    return {"message": "Book borrowed"}

@router.get("/return")
def return_book(book_id: str, user_id: str, db: Session = Depends(get_db)):
    loan = db.query(Loan).filter(Loan.user_id == user_id and Loan.book_id == book_id).first()

    if not loan or loan.returned_at:
        raise HTTPException(400, "Invalid loan")

    loan.returned_at = datetime.utcnow()

    book = db.query(Book).filter(Book.id == loan.book_id).first()
    book.available_copies += 1

    db.commit()

    return {"message": "Book returned"}


@router.get("/books")
def get_books(user_id: str | None = None, db: Session = Depends(get_db)):
    books = db.query(Book).all()

    result = []
    for book in books:
        loan = None

        if user_id:
            loan = db.query(Loan).filter(
                Loan.book_id == book.id,
                Loan.user_id == user_id,
                Loan.returned_at == None
            ).first()

        result.append({
            "id": book.id,
            "title": book.title,
            "available_copies": book.available_copies,
            "loan_id": loan.id if loan else None,
            "borrowed_by_user": loan is not None
        })

    return result


@router.get("/bookings")
def get_books(user_id: str | None = None, db: Session = Depends(get_db)):
    books = db.query(Book).all()

    result = []
    for book in books:
        loan = None

        if user_id:
            loan = db.query(Loan).filter(
                Loan.book_id == book.id,
                Loan.user_id == user_id,
                Loan.returned_at == None
            ).first()

        result.append(Loan.id)

    return result

