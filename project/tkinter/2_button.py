from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정

btn1 = Button(root, text="버튼1")  # root는 메인을 의미한다.
btn1.pack()  # pack을 해줘야 실제로 적용이 된다.

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # padx 는 x공간에 padding을 주는
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")  # 버튼의 크기를 고정시키는
btn4.pack()
# btn4번은 글자가 많아지면 글자가 짤림, btn2,3번은 같이 커진다.

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="D:\\python\\project\\tkinter\\image.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭 되었어요")


btn7 = Button(root, text="동작 하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()  # 창이 닫히지 않게 해주는 것
