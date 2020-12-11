# combobox는 따로 불러와야함
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

values = [str(i)+"일" for i in range(1, 32)]  # 1~31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정 / 버튼 클릭을 통한 값 설정도 가능

readonly_combobox = ttk.Combobox(
    root, height=5, values=values, state="readonly")
readonly_combobox.current(0)  # 0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않게 해주는 것
