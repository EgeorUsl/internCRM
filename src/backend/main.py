#!/usr/bin/python3
# from fastapi_users.router import get_current_active_user
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from core.models import db_helper, Base
import uvicorn
from core.email.email import router as email_router
from candidates.views import router as candidates_router
from interns.views import router as interns_router
from webform.views import router as webform_router
from users.views import router as users_router
from core.tests_forms.gforms import router as gforms_router
from config import settings
from core.auth.auth import fastapi_users
from users.schemas import UserRead, UserCreate
from core.auth.auth import auth_backend
from branches.views import router as branches_router
from cities.views import router as cities_router
from core.models.structure import create_base_structure
from status.views import router as status_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await create_base_structure()
    yield

app = FastAPI(lifespan=lifespan, prefix=f"{settings.web.API_PREFIX}")
app.include_router(email_router, prefix=f"{settings.web.API_PREFIX}")
app.include_router(candidates_router, prefix=f"{settings.web.API_PREFIX}")
app.include_router(cities_router, prefix=f"{settings.web.API_PREFIX}")
app.include_router(branches_router, prefix=f"{settings.web.API_PREFIX}")
app.include_router(users_router, prefix=f"{settings.web.API_PREFIX}")
app.include_router(interns_router, prefix=f"{settings.web.API_PREFIX}")
app.include_router(gforms_router, prefix=f"{settings.web.API_PREFIX}")
app.include_router(webform_router, prefix=f"{settings.web.API_PREFIX}")
app.include_router(status_router, prefix=f"{settings.web.API_PREFIX}")


origins = [f"http://{settings.web.DOMAIN}", f"https://{settings.web.DOMAIN}"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=f"{settings.web.API_PREFIX}/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=f"{settings.web.API_PREFIX}/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix=f"{settings.web.API_PREFIX}/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserCreate),
    prefix=f"{settings.web.API_PREFIX}/auth/users",
    tags=["users"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
