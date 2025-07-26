from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


class BookRepository:

    @staticmethod
    async def create(session: AsyncSession, book_data: BookCreate) -> Book:
        new_book = Book(**book_data.model_dump())
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    @staticmethod
    async def get_by_id(session: AsyncSession, book_id: int) -> Book | None:
        result = await session.execute(select(Book).where(Book.id == book_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[Book]:
        result = await session.execute(select(Book))
        return result.scalars().all()

    @staticmethod
    async def update(session: AsyncSession, book_id: int, book_data: BookUpdate) -> Book | None:
        result = await session.execute(select(Book).where(Book.id == book_id))
        book = result.scalar_one_or_none()

        if not book:
            return None

        for field, value in book_data.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        await session.commit()
        await session.refresh(book)
        return book

    @staticmethod
    async def delete(session: AsyncSession, book_id: int) -> bool:
        result = await session.execute(select(Book).where(Book.id == book_id))
        book = result.scalar_one_or_none()

        if not book:
            return False

        await session.delete(book)
        await session.commit()
        return True
