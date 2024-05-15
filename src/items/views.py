from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.engine import db_manager

from .schemas import Item, ItemCreate, ItemUpdate, ItemUpdatePartial
from .dependencies import item_by_id_dep
from .services import (
    get_items,
    create_item,
    update_item,
    delete_item
)

items_router = APIRouter(prefix='/items', tags=['Items'])


@items_router.get('/', response_model=list[Item])
async def get_items_view(
    session: AsyncSession = Depends(db_manager.session_dependecy)
):
    return await get_items(session)


@items_router.post('/', response_model=Item)
async def create_item_view(
    item: ItemCreate,
    session: AsyncSession = Depends(db_manager.session_dependecy)
    ):
    return await create_item(session, item)


@items_router.get('/{item_id}/', response_model=Item)
async def get_item_by_id_view(
    item: Item = Depends(item_by_id_dep)
):
    return item


@items_router.put('/{item_id}/')
async def recreate_item_by_id_view(
    item_update: ItemUpdate,
    session: AsyncSession = Depends(db_manager.session_dependecy),
    item: Item = Depends(item_by_id_dep)
):
    return await update_item(session, item, item_update)


@items_router.patch('/{item_id}/')
async def update_item_by_id_view(
    item_update: ItemUpdatePartial,
    session: AsyncSession = Depends(db_manager.session_dependecy),
    item: Item = Depends(item_by_id_dep)
):
    return await update_item(session, item, item_update, partial=True)


@items_router.delete('/{item_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_by_id_view(
    session: AsyncSession = Depends(db_manager.session_dependecy),
    item: Item = Depends(item_by_id_dep)
):
    return await delete_item(session, item)
