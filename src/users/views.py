from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from src.users.schemas import User
from src.users.services import user_to_dict

users_router = APIRouter(prefix='/users', tags=['Users'])


@users_router.post('/')
async def create_user(user: User):
    user_dict = await user_to_dict(user)
    json_data = jsonable_encoder(user_dict)
    return JSONResponse(json_data)


@users_router.get('/me/')
async def get_id():
    return {'id': 228}


@users_router.get('/{id}/')
async def get_id(id: int):
    return {'id': id}
