from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)  # 객체생성
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# with를 사용하게 되면, logout()도 따로 안해줘도 되고 한줄로 끝낼 수 있다.
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=10, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # '(UNSEEN)' : 읽지않은 메일, Query문
    # for msg in mailbox.fetch('(UNSEEN)', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # '(FROM email)' : 발신자를 기준으로 검색하는, Query문
    # for msg in mailbox.fetch('(FROM chlwhddls1224@gmail.com)', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # '(TEXT "찾고자하는 문자열")' : 찾고자 하는 문자열에 해당하는 것만 가져옴
    # for msg in mailbox.fetch('(TEXT "test")'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자를 포함하는 메일 (제목만)
    # for msg in mailbox.fetch('(SUBJECT "test")'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자(한글)을 포함하는 메일 필터링 (제목)  위에 방법은 한글검색은 못함 아스키 오류
    # for msg in mailbox.fetch(limit=10, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이후로온 메일 검색
    # '(SENTSINCE) 07-Nov-2020)'): 2020년 12월 7일 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # # 특정 날짜에 온 메일 검색
    # for msg in mailbox.fetch('(ON 25-Dec-2020)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건을 모두 만족하는 메일(and 조건)
    # for msg in mailbox.fetch('(ON 25-Dec-2020 FROM chlwhddls1224@gmail.com)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건 중 하나라도 만족하는 메일 (or 조건)
    for msg in mailbox.fetch('(OR ON 25-Dec-2020 ON 24-Dec-2020)'):
        print("[{}] {}".format(msg.from_, msg.subject))
