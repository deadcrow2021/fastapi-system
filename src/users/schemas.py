from pydantic import EmailStr, BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen



class User(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr
