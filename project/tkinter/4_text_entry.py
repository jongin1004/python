from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")  # 디폴트 txt값을 입력
# END입력될 위치를 선택 지금은 아무것도 없으니 처음부터 입력됨
e = Entry(root, width=30)  # enter불가, 한줄로 txt를 받을 경우
e.pack()
e.insert(0, "한 줄만 입력해요")  # 처음에 아무런 입력값이 없으니 index 0이나 END나 똑같이 처음부터 입력


def btncmd():
    # 내용출력
    print(txt.get("1.0", END))  # "1.0" 1은 첫번째 줄부터 가져와라 0은 0번째 컬럼부터 가져와라
    # 그래서 END 끝까지 다 가져와라
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않게 해주는 것
