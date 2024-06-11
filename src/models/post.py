from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text


from .mixins import UserRelationMixin


class Post(UserRelationMixin, Base):
    _user_back_populated = 'posts'

    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(
        Text,
        default='',
        server_default='',
    )

    def __str__(self) -> str:
        return f'Post(title={self.title}, user_id="{self.user_id}")'
    
    def __repr__(self) -> str:
        return str(self)
