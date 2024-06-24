from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from fastapi_users import FastAPIUsers
from core.models import User
from config import settings
from core.auth.manager import get_user_manager

cookie_transport = CookieTransport(
    cookie_name="internCRM", cookie_max_age=settings
    .authJWT.access_token_expire_seconds)


def get_jwt_strategy() -> JWTStrategy:
    with open(settings.authJWT.secret_sync, 'r') as f:
        secret = f.read().strip()
    return JWTStrategy(secret=secret,
                       lifetime_seconds=settings
                       .authJWT.access_token_expire_seconds)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
