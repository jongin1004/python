from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

checkvar = IntVar()  # Checkvar에 int형으로 값을 저장한다.
checkbox = Checkbutton(root, text="오늘하루 보지않기", variable=checkvar)
# checkbox.select()  # 자동 선택 처리
# checkbox.deselect()  # 선택 해제 처리
checkbox.pack()

checkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=checkvar2)
checkbox2.pack()


def btncmd():
    print(checkvar.get())  # 값이 0 : 체크 x 값이 1 : 체크 o

    print(checkvar2.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않게 해주는 것
