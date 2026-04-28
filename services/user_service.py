from sqlalchemy.orm import Session
from repository import user_repo

def list_books(db: Session):
    return user_repo.get_all_users(db)