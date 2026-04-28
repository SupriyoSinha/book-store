from pydantic import BaseModel

class BorrowRequest(BaseModel):
    book_id: str
    user_id: str