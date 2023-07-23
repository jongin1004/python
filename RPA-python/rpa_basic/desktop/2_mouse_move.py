import pyautogui

# 마우스 이동 (절대좌표 이동 )
# pyautogui.moveTo(100, 100) #지정한 위치로 마우스 이동 (가로, 세로)
# pyautogui.moveTo(100, 200, duration = 0.5) # 0.5초에 걸쳐서 마우스가 이동됨

# 마우스 이동 (상대좌표 이동) - 현재 마우스 위치를 기준
print(pyautogui.position())
pyautogui.move(300, 300)
print(pyautogui.position()) # 마우스이 좌표값  