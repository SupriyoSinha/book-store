from uuid import UUID

from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    price: float

class BookResponse(BookCreate):
    id: UUID

    class Config:
        from_attributes = True