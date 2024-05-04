from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}__table'

    id: Mapped[int] = mapped_column(primary_key=True)
