from sqlalchemy.exc import IntegrityError
from .db_helper import db_helper
from users.schemas import UserCreate
from . import City, Status, Role, Branch, Group, Intern
from sqlalchemy.ext.asyncio import AsyncSession
from core.auth.manager import get_user_manager
from config import settings
import contextlib
from core.auth.manager import get_user_db
from fastapi_users.exceptions import UserAlreadyExists

records = [
    Role(name="None", permissions={"": ""}),
    Role(id=2, name="Admin", permissions={"*": "*"}),
    City(city_name="Иркутск"),
    City(city_name="Ангарск"),
    Status(status_name="Прибыл"),
    Status(status_name="Выбыл"),
    Branch(branch_name="Frontend разработка"),
    Branch(branch_name="Backend разработка"),
    Group(group_name="Группа 1", branch_id=1),
    Group(group_name="Группа 2", branch_id=1),
    Group(group_name="Группа 3", branch_id=1),
    Group(group_name="Группа 1", branch_id=2),
    Group(group_name="Группа 2", branch_id=2),
    Intern(first_name="Кандидат",
           last_name="Кандидатович",
           email="candidate@candidate.com",
           studing_place="IEK",
           education="ВПО",
           status_id=1,
           city_id=1,
           branch_id=1,
           group_id=1,
           ),
    Intern(first_name="Иван",
           last_name="Иванович",
           email="candidate2@candidate.com",
           studing_place="",
           education="ВПО",
           status_id=1,
           city_id=1,
           branch_id=1,
           group_id=1,
           )
]

user_create = UserCreate(
    username="admin",
    email="test@example.com",
    password=settings.db.ADMIN_CRM,
    role_id=2,
    is_superuser=True,
    is_verified=True
)

get_async_session_context = contextlib.asynccontextmanager(
    db_helper.get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(user_create: UserCreate):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        user_create
                    )
                    return user
    except UserAlreadyExists:
        print(f"User {user_create} already exists")
        raise


async def create_base_structure(session: AsyncSession =
                                db_helper.session_factory(),
                                obj: list = records,
                                user: UserCreate = user_create):
    try:
        for i in obj:
            session.add(i)
        await session.commit()
    except IntegrityError:
        await session.rollback()
    try:
        await create_user(user)
    except UserAlreadyExists:
        print("user already exist")
