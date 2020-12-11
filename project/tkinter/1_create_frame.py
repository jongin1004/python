from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정
# root.geometry("640x480+300+100")  # 가로 x 세로 크기  + x좌표 + y좌표
root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 ( 창크기 변경 불가)

root.mainloop()  # 창이 닫히지 않게 해주는 것
