from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session
from app.schemas.book import BookCreate, BookRead, BookUpdate
from app.services.book import BookService

router = APIRouter(prefix="/books", tags=["Books"])


# Dependency to get a session
async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(
        book: BookCreate,
        session: AsyncSession = Depends(get_db_session)
):
    return await BookService.create_book(session, book)


@router.get("/", response_model=list[BookRead])
async def list_books(session: AsyncSession = Depends(get_db_session)):
    return await BookService.list_books(session)


@router.get("/{book_id}", response_model=BookRead)
async def get_book(book_id: int, session: AsyncSession = Depends(get_db_session)):
    book = await BookService.get_book(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookRead)
async def update_book(
        book_id: int,
        data: BookUpdate,
        session: AsyncSession = Depends(get_db_session)
):
    book = await BookService.update_book(session, book_id, data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, session: AsyncSession = Depends(get_db_session)):
    success = await BookService.delete_book(session, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
