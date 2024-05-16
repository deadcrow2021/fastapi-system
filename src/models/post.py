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
