import smtplib
from email.mime.text import MIMEText

EMAIL = "cintabumi@gmail.com"       # email pengirim
PASSWORD = "your_app_password"       # app password Gmail
TO_EMAIL = "ramatrusdi@gmail.com"    # email tujuan

def send_email():
    subject = "Pesan Otomatis dari GitHub"
    body = "Halo! Ini pesan otomatis yang dikirim GitHub pada pukul 15.06."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL

    # kirim email melalui SMTP Gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    send_email()
