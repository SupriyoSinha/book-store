from sqlalchemy.orm import Session
from models.book import Book

def create_book(db: Session, book_data):
    book = Book(**book_data.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_all_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: str):
    return db.query(Book).filter(Book.id == book_id).first()

def delete_book(db: Session, book_id: str):
    book = get_book_by_id(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book