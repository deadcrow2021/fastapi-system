from pydantic import EmailStr, BaseModel
from typing import Union, Annotated
from annotated_types import MinLen, MaxLen


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr
