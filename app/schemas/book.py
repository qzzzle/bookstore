from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    description: str | None = None
