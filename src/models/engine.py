from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.settings import settings

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


db_manager = DBManager(
    url = f'postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}/{settings.postgres_db}',
    echo=settings.postgres_debug
)
