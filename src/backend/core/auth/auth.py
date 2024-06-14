from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from config import settings

cookie_transport = CookieTransport(
    cookie_name="internCRM", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    with open(settings.authJWT.private_key_path, 'r') as f:
        secret = f.read().strip()
    return JWTStrategy(secret=secret,
                       lifetime_seconds=settings.authJWT.access_token_expire_seconds)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
