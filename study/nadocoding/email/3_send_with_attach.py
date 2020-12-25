import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()  # 객체 생성
msg["Subject"] = "테스트 메일입니다."  # 제목
msg["From"] = EMAIL_ADDRESS  # 보내는 사람
msg["To"] = "chlwhddls1224@gmail.com"  # 받는 사람
msg.set_content("다운로드 하세요")

# MIME TYPE  -> 인터넷 공간에 글을 올릴 때, type에 따라 등록하는 방식이 따로있다.
# 웹에서 사용할려는 컨텐츠의 type이 어떤 것인지 알려주는 것


# 첨부파일
# msg.add_attachment()

# txt파일
with open("김사원세끼.txt", "rb") as f:
    msg.add_attachment(f.read(), maintype="text",
                       subtype="plain", filename=f.name)

# pdf파일
with open("test.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application",
                       subtype="pdf", filename=f.name)
# xls파일
# with open("./study/test.xls", "rb") as f:
#     msg.add_attachment(f.read(), maintype="application",
#                        subtype="vnd.ms-excel", filename=f.name)


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
