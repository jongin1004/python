from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)


def create_new_file():
    print("새 파일을 만듭니다")


def create_new_window():
    print("새 창을 만듭니다")


# File 메뉴
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window", command=create_new_window)
menu_file.add_separator()  # 구분자 추가
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")  # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# Edit메뉴 (빈값)
menu.add_cascade(label="Edit")

# languge 메뉴 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="PHP")
menu.add_cascade(labe="languge", menu=menu_lang)

# View 메뉴 (check박스로 )
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)

root.mainloop()  # 창이 닫히지 않게 해주는 것
