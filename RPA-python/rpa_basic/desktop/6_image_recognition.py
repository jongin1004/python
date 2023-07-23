import pyautogui
import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

def optimize_coordinates(coordinates):
    left, top, width, height = coordinates
    new_left = left / 2 + width / 4
    new_top = top / 2 + height / 4
    return new_left, new_top

# 이미지를 찾기 못하는 경우에는 None
# file_menu = pyautogui.locateOnScreen('file_menu.png')
# left, top = optimize_coordinates(file_menu)
# debug_icon = pyautogui.locateOnScreen('debug_icon.png')
# left, top = optimize_coordinates(debug_icon)

# 이미지 찾는 속도 개선 
# 1. GrayScale를 사용하면 30% 개선 가능
# debug_icon = pyautogui.locateOnScreen('debug_icon.png', grayscale=True)

# 2. 범위 지정 (mac환경에서는 left와 top을 position값의 2배를 해야함)
# run_icon = pyautogui.locateOnScreen('run_icon.png', region=(4700, 100, 1000, 1000))

# 3. 정확도 조정
# debug_icon = pyautogui.locateOnScreen('debug_icon.png', confidence=0.5) # 50% 이상 일치하면 찾도록

# 자동화 대상이 바로 보여지지 않는 경우
# 1) 하염없이 기다리기
# create_icon = pyautogui.locateOnScreen('create_icon.png')
# while create_icon is None:
#     create_icon = pyautogui.locateOnScreen('create_icon.png')
    
# 2) timeout을 통해서, 빠져나가기
import time
import sys

timeout = 5
start   = time.time() # 시작 시간 설정

create_icon = None
# while create_icon is None:
#     create_icon = pyautogui.locateOnScreen('create_icon.png')
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout:
#         print('시간종료')
#         sys.exit()

def find_target(img_file, timeout):
    start  = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break

    return target

def clickImage(img_file, timeout = 10):
    target = find_target(img_file, timeout)
    if target:
        left, top = optimize_coordinates(target)
        pyautogui.click(left, top)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}).")

clickImage('create_icon.png', 5)

# left, top = optimize_coordinates(create_icon)
# pyautogui.click(left, top)
