from fastapi import Path, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from .services import get_user_by_id
from src.users.schemas import User
from src.models import db_manager


async def user_by_id_dep(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_manager.session_dependecy),
    ) -> User:
    user = await get_user_by_id(session, user_id)

    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with id {user_id} does not exist.'
    )

