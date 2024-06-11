from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession
)

from src.settings import db_settings


class DBManager:
    def __init__(self, url: str, echo: bool = False) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.async_session = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


    def _get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.async_session,
            scopefunc=current_task
        )
        return session


    async def session_dependecy(self) -> AsyncSession:
        session = self._get_scoped_session()
        yield session
        await session.close()


db_manager = DBManager(
    url = db_settings.db_url,
    echo = db_settings.db_debug
)
