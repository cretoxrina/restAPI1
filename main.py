from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # моделей данных
import smtplib # электронный пиьсма отправки 
import logging
import re

app = FastAPI()

class EmailRequest(BaseModel): # наследует от класса чтобы провреять валидацию
    to: str
    subject: str # это чисты тайп хинты атрибутов класса которые будем юзать 
    message: str

@app.post("/send_email")
async def send_email(email_request: EmailRequest):

    if not validate_email(email_request.to): # сперва чекаем эмейл если не тру то возвращаем эксепшн
        raise HTTPException(status_code=400, detail="Invalid email format")

    try:
        smtp_server = "smtp.gmail.com"  # использую гуглский, столько мароки было чтобы получить доступ
        smtp_port = 465
        smtp_username = "yerasylkenzhetay@gmail.com" # использую свой гмейл
        smtp_password = "dfzy yhja gqtz dskc" # получил доступ АПП ПАССУОРД

        with smtplib.SMTP(smtp_server, smtp_port) as server: # использую метод СМТП портом и сервером
            server.starttls()
            server.login(smtp_username, smtp_password)
            message = f"Subject: {email_request.subject}\n\n{email_request.message}"
            server.sendmail(smtp_username, email_request.to, message)
        return {"message": "Email sent succesfully"} # если отправлено успешно то возвращаю сообщение 
    except Exception as e:  # гененрирую эррор
        logging.error(str(e))
        raise HTTPException(status_code=500, detail="Failed to send email")

def validate_email(email):
    # Валидация эмейл через регулярные выражения по идее думал просто кортеж создать и оттуда проверять, но это гон
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None
