from sqlalchemy.orm import Mapped
from src.models.base import Base


class Item(Base):

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
