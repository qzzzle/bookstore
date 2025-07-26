from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.author import AuthorRepository
from app.schemas.author import AuthorCreate, AuthorRead


class AuthorService:

    @staticmethod
    async def create_author(session: AsyncSession, data: AuthorCreate) -> AuthorRead:
        author = await AuthorRepository.create(session, data)
        return AuthorRead.model_validate(author)

    @staticmethod
    async def get_author(session: AsyncSession, author_id: int) -> AuthorRead | None:
        author = await AuthorRepository.get_by_id(session, author_id)
        return AuthorRead.model_validate(author) if author else None

    @staticmethod
    async def list_authors(session: AsyncSession) -> list[AuthorRead]:
        authors = await AuthorRepository.get_all(session)
        return [AuthorRead.model_validate(a) for a in authors]
