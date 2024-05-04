from src.users.schemas import User
from typing import Dict, Any

async def user_to_dict(user: User) -> Dict[str, Any]:
    user_json = user.model_dump()
    return user_json