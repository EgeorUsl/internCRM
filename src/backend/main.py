#!/usr/bin/python3
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status
from core.models import db_helper, Base
import uvicorn
from core.auth.jwt_auth import router as auth_router
from core.email.email import router as email_router
from candidates.views import router as candidates_router
from config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
app.include_router(email_router)
app.include_router(candidates_router)

origins = [f"http://{settings.web.DOMAIN}", f"https://{settings.web.DOMAIN}"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/teapot",
    status_code=status.HTTP_418_IM_A_TEAPOT,
)
async def Teapot():
    return {"message": "I'm a teapot"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)