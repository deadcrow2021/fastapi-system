from fastapi import FastAPI
import uvicorn

from src.views import users_router

app = FastAPI()
app.include_router(users_router)

@app.get('/')
async def ok():
    return {'status': 'ok'}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000, reload=True)
