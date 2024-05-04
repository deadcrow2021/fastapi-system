from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from src.users.views import users_router
from src.models import Base, db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users_router)


@app.get('/')
async def ok():
    return {'status': 'ok'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000, reload=True)
