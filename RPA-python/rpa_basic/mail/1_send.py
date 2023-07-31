import smtplib
from config import *

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.ehlo() # 연결이 잘 수립되었는지 확인
    smtp.starttls() # 모든 내용을 암호화하여 전송
    smtp.login(MAIL_USERNAME, MAIL_PASSWORD) # 로그인

    subject = 'test mail'
    body    = 'mail body'

    # 정해진 양식으로 전달해야함 
    msg = f'Subject: {subject}\n{body}'
    smtp.sendmail(MAIL_USERNAME, MAIL_USERNAME, msg) # from, to, msg
