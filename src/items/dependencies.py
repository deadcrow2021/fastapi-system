from fastapi import HTTPException, status, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from .schemas import Item
from src.models.engine import db_manager
from .services import get_item_by_id


async def item_by_id_dep(
    item_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_manager.session_dependecy)
) -> Item:
    item = await get_item_by_id(session, item_id)

    if item is not None:
        return item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Item with id {item_id} does not exist.'
    )
