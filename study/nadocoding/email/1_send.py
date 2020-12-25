import smtplib  # 메일을 보내기위해 사용하는 라이브러리
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:  # 포트번호 587
    smtp.ehlo()  # smtp서버에 연결이 잘 수행되는지 확인
    smtp.starttls()  # 전송하는 모든 내용이 암호화
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # 로그인

    subject = "text mail"  # 메일 제목
    body = "mail body"  # 메일 본문

    msg = f"Subject: {subject}\n{body}"  # 메일 보낼 때에 정해진 틀이다 이건 정해진 것

    # 발신자, 수신자, 정해진 형식의 메세지
    smtp.sendmail(EMAIL_ADDRESS, "chlwhddls1224@gamil.com", msg)
