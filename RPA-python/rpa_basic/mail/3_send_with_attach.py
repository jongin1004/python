import smtplib
from config import *
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = '첨부파일'
msg['From']    = MAIL_USERNAME
msg['To']      = 'chlwhddls1224@gmail.com'
msg.set_content('첨부파일을 다운로드하세요')

# r: 읽기모드, b:바이너리 (사진파일)
with open('images/screenshot.png', 'rb') as f:
    # maintype/subtype = mime type
    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=f.name)

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.ehlo() # 연결이 잘 수립되었는지 확인
    smtp.starttls() # 모든 내용을 암호화하여 전송
    smtp.login(MAIL_USERNAME, MAIL_PASSWORD) # 로그인

    smtp.send_message(msg) # from, to, msg
