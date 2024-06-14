from .db_helper import db_helper
from . import Role
from users.schemas import UserCreate
from config import settings

roles = [
    Role(name="Admin", permissions={"all": "all"}),
    Role(name="Lead", permissions={"": ""})
]

# admin = UserCreate(
#     email=f"{settings.email.USERNAME}@{settings.email.SERVER}",
#     username="admin",
#     role_id=roles[0].id,  # Use the ID of the existing Admin role
#     password=settings.db.ADMIN_CRM,
#     is_active=True,
#     is_superuser=False,
#     is_verified=False
# )


async def create_base_structure(ses=db_helper.session_factory()):
    async with ses as session:
        async with session.begin():
            session.add_all(roles)
