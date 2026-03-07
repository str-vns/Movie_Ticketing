import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

def send_email(recipient_email: str, subject: str, body: str):
    mas = MIMEMultipart()
    mas['From'] = SENDER_EMAIL
    mas['To'] = recipient_email
    mas['Subject'] = subject
    mas.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(SENDER_EMAIL, [recipient_email], mas.as_string())
    except Exception as e:
        return {"error": str(e)}
            