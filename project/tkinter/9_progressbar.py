# combobox는 따로 불러와야함
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

# progressbar는 진행상태를 알려줄 경우에 사용
# indeterminate 정해지지 않은 , 언제 끝날지 모른다.
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # 10ms 마다 움직임 / 실행을 시켜줌
# progressbar.pack()


# def btncmd():
#     progressbar.stop()  # 작동 중지


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()  # 진행값은 실수로도 진행 될 수 있기 때문에 Double
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):  # 1~100
        time.sleep(0.01)  # 0.01초 대기

        p_var2.set(i)  # progress bar 의 값 설정
        progressbar2.update()  # for문이 동작할 때마다 ui적으로 업데이트 시켜줌
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()  # 창이 닫히지 않게 해주는 것
