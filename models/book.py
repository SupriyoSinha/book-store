from numbers import Number

from sqlalchemy import Column, String, Float ,Numeric
from db.base import Base
import uuid

class Book(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    available_copies = Column(Numeric, nullable=False)


