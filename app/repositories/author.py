from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.author import Author
from app.schemas.author import AuthorCreate


class AuthorRepository:

    @staticmethod
    async def create(session: AsyncSession, data: AuthorCreate) -> Author:
        author = Author(**data.model_dump())
        session.add(author)
        await session.commit()
        await session.refresh(author)
        return author

    @staticmethod
    async def get_by_id(session: AsyncSession, author_id: int) -> Author | None:
        result = await session.execute(
            select(Author).where(Author.id == author_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[Author]:
        result = await session.execute(select(Author))
        return result.scalars().all()
