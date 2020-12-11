import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

# 에러가 떳을 때 팝업이 뜨는 것이 메세지

# 기차 예매 시스템이라고 가정


def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")  # showinfo("알림타이틀", "알림 내용")


def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")


def error():
    msgbox.showerror("에러", "결제오류가 발생했습니다.")


def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?.")


def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

    print("응답 :", response)
    if response == 1:  # 네 ok
        print("재시도")

    elif response == 0:  # 아니요
        print("취소")


def yesno():
    msgbox.askyesno("예 / 아니요", "해당 좌석은 역방향입니다. 예매하시겠습니까?")


def yesnocancel():
    response = msgbox.askyesnocancel(
        title=None, message="예매 내역이 저장되지 않았습니다.\n 저장후 프로그램을 종료하시겠습니까?")

    print("응답 :", response)
    if response == 1:  # 네 ok
        print("예")

    elif response == 0:  # 아니요
        print("아니요")

    else:
        print("취소")

# 네 : 저장후 종료
# 아니요 : 저장하지 않고 종료
# 취소 : 프로그램 종료 취소 ( 현재 화면 계속 작업)


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인취소").pack()
Button(root, command=retrycancel, text="재시도취소").pack()
Button(root, command=yesno, text="예 아니요").pack()
Button(root, command=yesnocancel, text="예 아니요 취소").pack()


root.mainloop()  # 창이 닫히지 않게 해주는 것
