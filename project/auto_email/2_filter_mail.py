from imap_tools import MailBox
from account import *

application_list = []  # 지원자 리스트

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1  # 순번
    for msg in mailbox.fetch('(SENTSINCE 25-Dec-2020)'):  # 2020년 12월 25일 이후로 온 메일 조회
        if "파이썬 특강 신청입니다." in msg.subject:
            name, phone = msg.text.strip().split("/")
            print(index, name, phone)
            application_list.append((msg, index, name, phone))  # 튜플식으로 넣는다.
            index += 1

for application in application_list:
    print(application)
