from pydantic import BaseModel, ConfigDict
from typing import Union

class ItemBase(BaseModel):

    name: str
    description: str
    price: int


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemUpdatePartial(BaseModel):

    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[int, None] = None


class Item(ItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
