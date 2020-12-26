import random
import smtplib
from imap_tools import MailBox
from account import *
from email.message import EmailMessage

names = ["유재석", "박명수", "정형돈", "노홍철", "길"]

# for name in names:
#     msg = EmailMessage()  # 객체 생성
#     msg["Subject"] = "파이썬 특강 신청입니다."  # 제목
#     msg["From"] = EMAIL_ADDRESS  # 보내는 사람
#     msg["To"] = "chlwhddls1224@gmail.com"  # 받는 사람

#     number = str(random.randint(0, 9999))
#     msg.set_content("{}/{}".format(name, number.zfill(4)))  # 메일 본문

#     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()
#         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         smtp.send_message(msg)

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    for idx, msg in enumerate(mailbox.fetch(limit=10, reverse=True)):
        if "파이썬 특강 신청" in msg.subject:
            if idx < 10:
                msg2 = EmailMessage()
                msg2["Subject"] = "파이썬 특강 안내 [탈락]"  # 제목
                msg2["From"] = EMAIL_ADDRESS  # 보내는 사람
                msg2["To"] = msg.from_  # 받는 사람

                name = msg.text.split("/")
                msg2.set_content(
                    "{}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {}번)".format(name[0], 2-idx))

                with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg2)

            # else :
            #   msg2 = EmailMessage()
            #     msg2["Subject"] = "파이썬 특강 안내 [선정]"  # 제목
            #     msg2["From"] = EMAIL_ADDRESS  # 보내는 사람
            #     msg2["To"] = msg.from_  # 받는 사람

            #     name = msg.text.split("/")
            #     msg2.set_content(
            #         "{}님 축하드립니다. 특강 대상자로 선정되셨습다. (선정순정 {}번)".format(name[0], idx+1))

            #     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            #         smtp.ehlo()
            #         smtp.starttls()
            #         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            #         smtp.send_message(msg2)
