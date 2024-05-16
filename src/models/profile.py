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
