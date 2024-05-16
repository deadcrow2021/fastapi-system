from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .post import Post

class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)

    posts: Mapped[list['User']] = relationship(back_populates='user')
