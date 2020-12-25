import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()  # 객체 생성
msg["Subject"] = "테스트 메일입니다."  # 제목
msg["From"] = EMAIL_ADDRESS  # 보내는 사람
msg["To"] = "chlwhddls1224@gamil.com"  # 받는 사람

# 여러 명에게 메일을 보낼 때
# msg["To"] = "chlwhddls1224@gmail.com, chlwhddls1224@gmail.com"
# #list를 이용해서 여러명에게 보낼 때
# to_list = ["chlwhddls1224@gmail.com", "두번째 메일", "세번째 메일"]
# msg["To"] = ", ".join(to_list)

# 참조 - 수신인은 아니고 메일과 관련된 사람들
# msg["Cc"] = "chlwhddls1224@gmail.com"
# msg.set_content("테스트 본문입니다.")  # 메일 본문

# #비밀참조
# msg["Bcc"] = "chlwhddls1224@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
