from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent


class DBSettings(BaseSettings):
    URL: str = ""
    ECHO: bool = False
    # Password admin user for CRM-system
    ADMIN_CRM: str = "password"
    model_config = SettingsConfigDict(env_file_encoding='utf-8',
                                      env_prefix="DB_",
                                      extra="ignore",
                                      env_file=f"{BASE_DIR}/.env")


class AuthJWT(BaseSettings):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30

    model_config = SettingsConfigDict(env_file_encoding='utf-8',
                                      extra="ignore",
                                      env_prefix="JWT_",
                                      env_file=f"{BASE_DIR}/.env")


class EmailServer(BaseSettings):
    USERNAME: str = ""
    HOST: str = "localhost"
    PORT: int = 587
    PASSWORD: str = ""
    SSL_TLS: bool = True
    PATH_TEMPLATE: str = ""

    model_config = SettingsConfigDict(env_file_encoding='utf-8',
                                      extra="ignore",
                                      env_prefix="EMAIL_",
                                      env_file=f"{BASE_DIR}/.env")


class GoogleForms(BaseSettings):
    USERNAME: str = ""
    PASSWORD: str = ""

    model_config = SettingsConfigDict(env_file_encoding='utf-8',
                                      env_prefix="GOOGLEF_",
                                      extra="ignore",
                                      env_file=f"{BASE_DIR}/.env")


class Web(BaseSettings):
    DOMAIN: str = "localhost:8000"

    model_config = SettingsConfigDict(env_file_encoding='utf-8',
                                      env_prefix="WEB_",
                                      extra="ignore",
                                      env_file=f"{BASE_DIR}/.env")


class Settings(BaseModel):
    db: DBSettings = DBSettings()
    email: EmailServer = EmailServer()
    google_forms: GoogleForms = GoogleForms()
    authJWT: AuthJWT = AuthJWT()
    web: Web = Web()


settings = Settings()
