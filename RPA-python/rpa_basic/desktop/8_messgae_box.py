import pyautogui
import os

# 자동화 시작전에 카운터 다운을 출력해줌 3 2 1 
# pyautogui.countdown(3)
# print('자동화 시작')

#
# pyautogui.alert('자동화 수행이 완료되었습니다. 체크해주세요', '경고')
# result = pyautogui.confirm('계속 진행하시겠습니까?', '확인')
# print(result)

# result = pyautogui.prompt('파일명을 입력해주세요.', '입력')

result = pyautogui.password('암호를 입력하세요')