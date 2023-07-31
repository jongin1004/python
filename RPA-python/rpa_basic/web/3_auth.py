from selenium import webdriver
import json
import time

# 웹 드라이버 객체 생성
driver = webdriver.Chrome()

# 웹 페이지로 이동
driver.get('https://user:test@adsfactory.ne.jp/test/jrsec/')

# # execute_script() 메서드를 사용하여 JSON 데이터를 스크립트로 실행
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# # 잠시 대기 (페이지가 로드되기를 기다리는 시간을 넣으세요)
# driver.implicitly_wait(5)

# 이후부터는 페이지에 접근하여 작업할 수 있습니다.
# 예를 들어 페이지 요소를 찾아 작업하거나 클릭할 수 있습니다.

time.sleep(20)

# 웹 드라이버 종료
driver.quit()




