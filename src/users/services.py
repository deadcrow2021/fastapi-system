from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any

from src.users.schemas import User as scheme_user
from src.models import User


async def user_to_dict(user: scheme_user) -> Dict[str, Any]:
    user_json = user.model_dump()
    return user_json


async def get_users(session: AsyncSession) -> list[User]:
    query = select(User).order_by(User.id)
    res = await session.execute(query)
    users = res.scalars().all()
    return users


async def get_user_by_id(
    session: AsyncSession,
    user_id: int
    ) -> User:
    return await session.get(User, user_id)
