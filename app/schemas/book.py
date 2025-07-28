from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author_id: int
    description: str | None = None

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True

class BookUpdate(BaseModel):
    title: str | None = None
    author: int | None = None
    description: str | None = None
