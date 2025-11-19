import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =======================================================
# KONFIGURASI EMAIL
# =======================================================
email_pengirim = "ramatrusdi@gmail.com"
password_app = "PASSWORD_APLIKASI_16_DIGIT"
email_tujuan = "ramatrusdi@gmail.com"  # bisa email lain

# =======================================================
# FUNGSI KIRIM EMAIL
# =======================================================
def kirim_email():
    subject = "Pesan Otomatis dari Python"
    body = "Halo! Ini pesan otomatis yang dikirim Python pada pukul 14:46."

    msg = MIMEMultipart()
    msg["From"] = email_pengirim
    msg["To"] = email_tujuan
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_pengirim, password_app)
        server.sendmail(email_pengirim, email_tujuan, msg.as_string())
        server.quit()
        print("Email berhasil dikirim!")
    except Exception as e:
        print("Gagal mengirim email:", e)

# =======================================================
# JADWALKAN PADA 14:48
# =======================================================
schedule.every().day.at("14:53").do(kirim_email)

print("Program berjalan, menunggu pukul 14:46...")

# =======================================================
# LOOPING AGAR PROGRAM TETAP HIDUP
# =======================================================
while True:
    schedule.run_pending()
    time.sleep(1)

