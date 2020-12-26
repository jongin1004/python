from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)  # 객체생성
# initial_folder="INBOX" 받은 편지함을 의미
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# fetch는 모든 메일을 다가져온다
# limit는 최대 갯수 제한
# reverse=True를 해주면 최신것 부터 받아옴 ,False는 과거 메일부터 , 기본값은 False
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜", msg.date)  # GMT-8 로스엔젤러스 시간기준으로 나온다.
    print("본문", msg.text)
    print("HTML 메세지", msg.html)
    print("=" * 30)

    # 첨부 파일
    for att in msg.attachments:
        print("첨부파일 이름", att.filename)
        print("첨부파일 타입", att.content_type)
        print("첨부파일 크기", att.size)

        # 파일 다운로드
        with open("download_"+att.filename, "wb") as f:
            f.write(att.payload)  # payload 파일에다가 첨부파일을 쓰는 것
            print("첨부파일 {} 다운로드 완료".format(att.filename))
mailbox.logout()
