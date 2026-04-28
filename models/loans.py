from sqlalchemy import Column, String, Float, Date
from db.base import Base
import uuid

class Loan(Base):
    __tablename__ = "loans"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False)
    book_id = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)

