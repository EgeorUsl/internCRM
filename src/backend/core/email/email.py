from starlette.responses import JSONResponse
from fastapi import APIRouter
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from config import settings
from pydantic import EmailStr, BaseModel
from typing import List

router = APIRouter(prefix="/email",
                   tags=["E-MAIL"])


class EmailSchema(BaseModel):
    email: List[EmailStr]
    subject: str
    body: str


@router.post("/send")
async def simple_send(letter: EmailSchema) -> JSONResponse:
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.email.USERNAME,
        MAIL_PASSWORD=settings.email.PASSWORD,
        MAIL_FROM=f"{settings.email.USERNAME}@gmail.com",
        MAIL_PORT=settings.email.PORT,
        MAIL_SERVER=settings.email.HOST,
        MAIL_SSL_TLS=settings.email.SSL_TLS,
        MAIL_STARTTLS=True,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True
    )
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=letter.email,
        body=letter.body,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200,
                        content={"message": "email has been sent"})
