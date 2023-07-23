import pyautogui

# vsc의 파일 도구의 위치를 알아내고 
# pyautogui.sleep(3)
# print(pyautogui.position()) 

# 파일 도구를 클릭
# pyautogui.click(123, 15)

# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks = 2) # 클릭회수 지정

# pyautogui.rightClick()
# pyautogui.middleClick() # 휠 클릭
# 200, 200 위치에서 300, 300 로 드래그
# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()
# 드래그 사용시에, 속도가 빨라서 제대로 동작하지 않는 경우에는 duration을 추가해준다. 
# pyautogui.drag(100, 0) # 현재 마우스 위치를 기준으로 (100, 0) 위치로 드래그해서 이동
# pyautogui.dragTo(300, 300) # 절대 좌표 위치로 드래그를 함 

pyautogui.scroll(-300) # 위 방향으로 300만큼 스클롤 (-는 방향 반대)