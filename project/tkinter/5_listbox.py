from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

listbox = Listbox(root, selectmode="extended", height=0)  # single은 한가지만  선택가능
# extended는 여러개 선택가능
# height 값이 0이되면 리스트에 포한된것을 전부 한번에 보여줌
# 만약 3으로 지정하면 3칸만 보여주고 나머지는 스크롤로 볼 수 있게됨
listbox.insert(0, "딸기")  # insert값을 추가할 때
listbox.insert(1, "사과")
listbox.insert(2, "딸기")
listbox.insert(END, "수박")  # END는 가장 마지막에 넣어주겠다는 의미
listbox.insert(END, "바나나")
listbox.pack()


def btncmd():
    # listbox.delete(END)  # END 맨 뒤에 항목을 삭제 ,0 맨 앞 항목 삭제

    # # 개수 확인
    # print("리스트에느 ", listbox.size(), "개가 있어요")

    # 항목 확인
    # print("1번째 부터 3번째까지의 항복 : ", listbox.get(0, 2)) #시작과 끝 index를  지정

    # 선택된 항목 확인(index 위치로 반환)
    print("선택된 항목 : ", listbox.curselection())  # 항목이 index값으로 반환한다.


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않게 해주는 것
