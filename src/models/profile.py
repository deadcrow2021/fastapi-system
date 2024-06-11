from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

from .mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populated = 'profile'

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))

    user_id: Mapped[int] = mapped_column(
        ForeignKey('user__table.id'),
        unique=True
    )

    def __str__(self) -> str:
        return f'Profile(first_name={self.first_name}, last_name="{self.last_name}, user_id={self.user_id}")'
    
    def __repr__(self) -> str:
        return str(self)
