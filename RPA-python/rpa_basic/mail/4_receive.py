from imap_tools import MailBox
from config import *

mailbox = MailBox(IMAP_SERVER, IMAP_PORT)
# initial_folder: 가져올 받은 편지함 선택
mailbox.login(MAIL_USERNAME, MAIL_PASSWORD, initial_folder='INBOX')

# reverse=True: 최신순
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    print("참조", msg.cc)
    print("비밀참조", msg.bcc)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("HTML메세지", msg.html)

    for att in msg.attachments:
        filename = att.filename.split('/')[1]

        print('첨부파일 이름', filename)
        print('타입', att.content_type)
        print('크기', att.size)

        with open('download_from_mail_' + filename, 'wb') as f:
            f.write(att.payload)
            print(f'첨부파일 다운로드 완료 {filename}')

mailbox.logout()