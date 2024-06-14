#!/usr/bin/python3
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status
from core.models import db_helper, Base
import uvicorn
from core.email.email import router as email_router
from candidates.views import router as candidates_router
# from interns.views import router as interns_router
from webform.views import router as webform_router
from users.views import router as users_router
from core.tests_forms.gforms import router as gforms_router
from config import settings
from fastapi_users import fastapi_users, FastAPIUsers
from core.auth.manager import get_user_manager
from users.schemas import UserRead, UserCreate
from core.models import User
from core.auth.auth import auth_backend
from branches.views import router as branches_router
from cities.views import router as cities_router
# from core.models import create_base_structure


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # await create_base_structure()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(email_router)
app.include_router(candidates_router)
app.include_router(cities_router)
app.include_router(branches_router)
app.include_router(users_router)
# app.include_router(interns_router)
app.include_router(gforms_router)
app.include_router(webform_router)


origins = [f"http://{settings.web.DOMAIN}", f"https://{settings.web.DOMAIN}"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get(
    "/teapot",
    status_code=status.HTTP_418_IM_A_TEAPOT,
)
async def Teapot():
    return {"message": "I'm a teapot"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
