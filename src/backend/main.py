from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status
from core.models import db_helper, Base
import uvicorn
from core.auth.jwt_auth import router as auth_router
from core.email.email import router as email_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "https://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(email_router)


@app.get(
    "/teapot",
    status_code=status.HTTP_418_IM_A_TEAPOT,
)
async def Teapot():
    return {"message": "I'm a teapot"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
