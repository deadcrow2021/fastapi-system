from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.schemas import User
from src.users.services import user_to_dict
from src.models import db_manager
from .services import get_users
from .dependencies import user_by_id_dep


users_router = APIRouter(prefix='/users', tags=['Users'])


@users_router.get('/', response_model=list[User])
async def get_all_users(
    session: AsyncSession = Depends(db_manager.session_dependecy)
    ):
    return await get_users(session)


@users_router.post('/')
async def create_user(user: User):
    user_dict = await user_to_dict(user)
    json_data = jsonable_encoder(user_dict)
    return JSONResponse(json_data)


@users_router.get('/{id}/', response_model=User)
async def get_user_by_id(
    user = Depends(user_by_id_dep),
    ):
    return user
