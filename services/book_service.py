from sqlalchemy.orm import Session
from repository import book_repo

def create_book(db: Session, book):
    return book_repo.create_book(db, book)

def list_books(db: Session):
    return book_repo.get_all_books(db)

def get_book(db: Session, book_id: str):
    return book_repo.get_book_by_id(db, book_id)

def delete_book(db: Session, book_id: str):
    return book_repo.delete_book(db, book_id)