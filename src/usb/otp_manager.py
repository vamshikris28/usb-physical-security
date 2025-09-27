import random
import string
import smtplib
from email.mime.text import MIMEText
from usb_physical_security.utils import get_env_var, mask_email

def generate_otp(length=6):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))

def send_otp_email(receiver_email, otp):
    smtp_server = get_env_var("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(get_env_var("SMTP_PORT", 587))
    smtp_user = get_env_var("SMTP_USER")
    smtp_pass = get_env_var("SMTP_PASS")

    msg = MIMEText(f"Your OTP is: {otp}")
    msg["Subject"] = "USB Security OTP"
    msg["From"] = smtp_user
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
            print(f"OTP sent to {mask_email(receiver_email)}")
    except Exception as e:
        print(f"Failed to send OTP: {e}")
