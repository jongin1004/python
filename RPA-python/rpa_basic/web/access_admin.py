import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *
from selenium.webdriver.chrome.options import Options

# Chrome WebDriver 설정
chrome_options = Options()
chrome_options.add_argument("--headless")

# 웹 드라이버 객체 생성
driver = webdriver.Chrome(options=chrome_options)

# 웹 페이지로 이동
driver.get(f'https://{AUTH_ID}:{AUTH_PW}@{ADMIN_URL}newlist')

# # execute_script() 메서드를 사용하여 JSON 데이터를 스크립트로 실행
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 파일 업로드를 위한 input 태그의 XPath를 지정
file_input = driver.find_element(By.XPATH, '//*[@id="main_form"]/input[1]')

# 로컬 파일 경로를 입력하여 파일 업로드
file_input.send_keys(DOWNLOAD_PATH + "diff_20230731.csv")

# 업로드 버튼 또는 업로드 동작 실행
driver.find_element(By.XPATH, '//*[@id="main_form"]/input[2]').click()

time.sleep(10)
# 웹 드라이버 종료
driver.quit()




