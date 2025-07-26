from fastapi import FastAPI

from app.api.v1.routes import book

app = FastAPI(title="Bookstore API")

app.include_router(book.router)
