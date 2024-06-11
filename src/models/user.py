from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import EmailType
from sqlalchemy import String
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .post import Post
    from .profile import Profile

class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(EmailType, unique=True)
    password: Mapped[str] = mapped_column(String(32))

    posts: Mapped[list['Post']] = relationship(back_populates='user')
    profile: Mapped['Profile'] = relationship(back_populates='user')

    def __str__(self) -> str:
        return f'User(id={self.id}, username="{self.username}")'
    
    def __repr__(self) -> str:
        return str(self)
