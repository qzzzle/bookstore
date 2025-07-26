from typing import Optional, List

from pydantic import BaseModel

from app.schemas.book import BookRead


class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorRead(AuthorBase):
    id: int

    class Config:
        from_attributes = True


class AuthorWithBooks(AuthorRead):
    books: List[BookRead] = []
