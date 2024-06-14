# from app.config import HOST, USERNAME, PASSWORD, PORT, MailBody
# from ssl import create_default_context
# from email.mime.text import MIMEText
# from smtplib import SMTP
#
#
# def send_mail(data: dict | None = None):
#     msg = MailBody(**data)
#     message = MIMEText(msg.body, "html")
#     message["From"] = USERNAME
#     message["To"] = ",".join(msg.to)
#     message["Subject"] = msg.subject
#
#     ctx = create_default_context()
#
#     try:
#         with SMTP(HOST, PORT) as server:
#             server.ehlo()
#             server.starttls(context=ctx)
#             server.ehlo()
#             server.login(USERNAME, PASSWORD)
#             server.send_message(message)
#             server.quit()
#         return {"status": 200, "errors": None}
#     except Exception as e:
#         return {"status": 500, "errors": e}

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
        MAIL_FROM=settings.email.FROM,
        MAIL_PORT=settings.email.PORT,
        MAIL_SERVER=settings.email.SERVER_SMTP,
        MAIL_SSL_TLS=settings.email.SSL_TLS,
        MAIL_STARTTLS=not settings.email.SSL_TLS,
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
