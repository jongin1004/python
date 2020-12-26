import smtplib
import random
from account import *
from email.message import EmailMessage

names = ["유재석", "박명수", "정형돈", "노홍철", "길"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for name in names:
        msg = EmailMessage()  # 객체 생성
        msg["Subject"] = "파이썬 특강 신청입니다."  # 제목
        msg["From"] = EMAIL_ADDRESS  # 보내는 사람
        msg["To"] = "chlwhddls1224@gmail.com"  # 받는 사람

        number = str(random.randint(0, 9999))
        msg.set_content("{}/{}".format(name, number.zfill(4)))
        smtp.send_message(msg)
        print(name + "님으로부터 메일 받음")
