#파일 존재유무 확인 하기 위해서 
import os

# Quiz) tkinter 를 이용한 메모장 프로그램을 만드시요

# [GUI 조건]
# 1. title : 제목 없음 - Windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 ststus 바는 필요없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정이 가능해야함
# 7. 본문 우측에 상하 스크롤 바 넣기

from tkinter import *

root = Tk()
root.title("제목 없음 - Window 메모장")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)

filename = "mynote.txt"

def File_Open():
    # mynote = open("mynote.txt", "r", encoding="utf8")
    # lines = mynote.readlines()  # list형태로 저장
    # for line in lines:
    #     text.insert(END, line)

    # mynote.close()
    if os.path.isfile(filename): #파일이 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            text.delete("1.0", END) #기존 본문 내용을 삭제하고 파일만 불러오도록
            text.insert(END, file.read())


def File_Save():
    # mynote = open("mynote.txt", "w", encoding="utf8")
    # mynote.write(text.get("1.0", END))
    # mynote.close()

    with open(filename, "w", encoding="utf8") as file:
        file.write(text.get("1.0", END))


# File 메뉴
menu_file.add_command(label="File Open", command=File_Open)
menu_file.add_command(label="File Save", command=File_Save)
menu_file.add_separator()
menu_file.add_command(label="system Off", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# 나머지 메뉴들
menu.add_cascade(label="edit")
menu.add_cascade(label="view")

# 위젯이 text하나 밖에없기 때문에 frmae을 안써도 된다.
# frame 생성
# frame = Frame(root)
# frame.pack()

# scrollbar 위젯 생성
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# text위젯 생성
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True)

# scrollbar와 text창 맵핑
scrollbar.config(command=text.yview)


root.config(menu=menu)

root.mainloop()  # 창이 닫히지 않게 해주는 것
