from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.book import BookRepository
from app.schemas.book import BookCreate, BookRead, BookUpdate


class BookService:

    @staticmethod
    async def create_book(session: AsyncSession, data: BookCreate) -> BookRead:
        book = await BookRepository.create(session, data)
        return BookRead.model_validate(book)

    @staticmethod
    async def get_book(session: AsyncSession, book_id: int) -> BookRead | None:
        book = await BookRepository.get_by_id(session, book_id)
        return BookRead.model_validate(book) if book else None

    @staticmethod
    async def list_books(session: AsyncSession) -> list[BookRead]:
        books = await BookRepository.get_all(session)
        return [BookRead.model_validate(book) for book in books]

    @staticmethod
    async def update_book(session: AsyncSession, book_id: int, data: BookUpdate) -> BookRead | None:
        updated_book = await BookRepository.update(session, book_id, data)
        return BookRead.model_validate(updated_book) if updated_book else None

    @staticmethod
    async def delete_book(session: AsyncSession, book_id: int) -> bool:
        return await BookRepository.delete(session, book_id)
