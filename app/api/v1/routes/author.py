from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session
from app.schemas.author import AuthorCreate, AuthorRead
from app.services.author import AuthorService

router = APIRouter(prefix="/authors", tags=["Authors"])


# Dependency to get DB session
async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@router.post("/", response_model=AuthorRead, status_code=status.HTTP_201_CREATED)
async def create_author(
        data: AuthorCreate,
        session: AsyncSession = Depends(get_db_session)
):
    return await AuthorService.create_author(session, data)


@router.get("/", response_model=list[AuthorRead])
async def list_authors(session: AsyncSession = Depends(get_db_session)):
    return await AuthorService.list_authors(session)


@router.get("/{author_id}", response_model=AuthorRead)
async def get_author(author_id: int, session: AsyncSession = Depends(get_db_session)):
    author = await AuthorService.get_author(session, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author
