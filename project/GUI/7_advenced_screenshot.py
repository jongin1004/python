# 사용자가 입력한 keyboard값을 받아서 처리할 수 있는 것(후킹)
# 그러기 위해서 필요한 keyboard모듈
import keyboard
import time
from PIL import ImageGrab


def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("D:\\python\\basics\\image{}.png".format(curr_time))  # image_20200601_102030 .png


keyboard.add_hotkey("F9", screenshot)  # 사용자가 F9번을 입력했을 때 screenshot 함수를 동작
# 복합적인 키로 해도 동작
# keyboard.add_hotkey("ctrl+shift+s", screenshot)

keyboard.wait("esc")  # 사용자가 esc를 누르기 전까지 프로그램 수행
