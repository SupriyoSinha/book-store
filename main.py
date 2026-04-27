from fastapi import FastAPI
from api.v1 import book_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Bookstore API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(book_routes.router, prefix="/api/v1")