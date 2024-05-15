from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from typing import Union

from src.models.items import Item
from .schemas import ItemCreate, ItemUpdate


async def get_items(session: AsyncSession) -> list[Item]:
    query = select(Item).order_by(Item.id)
    result: Result = await session.execute(query)
    products = result.scalars().all()
    return list(products)


async def get_item_by_id(session: AsyncSession, id: int) -> Union[Item, None]:
    return await session.get(Item, id)


async def create_item(session: AsyncSession, item_in: ItemCreate) -> Item:
    item = Item(**item_in.model_dump())
    try:
        session.add(item)
    except:
        await session.rollback()
    else:
        await session.commit()
        # await session.refresh()
    
    return item


async def update_item(
        session: AsyncSession,
        item: Item,
        item_update: ItemUpdate,
        partial=False
):
    for key, val in item_update.model_dump(exclude_unset=partial).items():
        setattr(item, key, val)
    
    await session.commit()
    return item


async def delete_item(
        session: AsyncSession,
        item: Item,
):
    await session.delete(item)
    await session.commit()
