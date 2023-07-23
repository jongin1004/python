import pyautogui
import os

# os.system("open /Applications/Microsoft\ Excel.app")

pyautogui.sleep(2)

# pyautogui.write('asd')

# left는 방향키 왼쪽, enter는 키보드 enter
# interval는 각 키보드 입력사이에 지연시간을 줄 수 있다. 
# automatetheboringstuff.com chapter - 20에서 keyboard attribute 테이블통해 각 문자열의 의미를 확인할 수 있다.
# pyautogui.write(['t', 'e', 's', 't', 'left', 'left', 'enter'], interval=0.5)

# 특수문자 shift 4 = $
pyautogui.keyDown('shift')
pyautogui.press('4') # press = down + up
pyautogui.keyUp('shift')

# pyautogui.keyDown('command')
# pyautogui.press('a')
# pyautogui.keyUp('command')

# command 누르고 > a 누르고 > a 떼고 > command 떼고 
pyautogui.hotkey('command', 'a')

# 문장을 clip보드에 저장할 수 있도록 (한국어나, 일본어등 pyautogui에서 지원하지 않는 것을 입력할 수 있음)
# pip3 install pyperclip 
import pyperclip

pyperclip.copy('日本語') # 글자를 클립보드에 저장
pyautogui.hotkey('command', 'v')

# 자동화 프로그램 종료하고 싶은 경우
# win : ctrl + alt + del
# mac : cmd + shift + option + q