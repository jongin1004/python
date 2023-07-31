import smtplib
from config import *
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = '테스트 메일'
msg['From']    = MAIL_USERNAME
# msg['To']      = 'chlwhddls1224@gmail.com'
msg.set_content('테스트 본문내용')

# 여러명에게 전달
# msg['To'] = 'chlwhddls1224@gmail.com, bill1224@naver.com'
to_list = ['chlwhddls1224@gmail.com', 'bill1224@naver.com']
msg['To'] = ", ".join(to_list)

# 참조
# msg['Cc'] = '이메일'

# 비밀참조
# msg['Bcc'] = '이메일'

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.ehlo() # 연결이 잘 수립되었는지 확인
    smtp.starttls() # 모든 내용을 암호화하여 전송
    smtp.login(MAIL_USERNAME, MAIL_PASSWORD) # 로그인

    smtp.send_message(msg) # from, to, msg
