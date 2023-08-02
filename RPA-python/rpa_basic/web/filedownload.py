import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from config import *

# Chrome WebDriver 설정
chrome_options = Options()
chrome_options.add_argument("--headless")
# 다운로드를 위해 설정 추가
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": DOWNLOAD_PATH,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options) # 인자를 생략하면, 자동적으로 동일한 path에서 드라이버를 찾음 

driver.get(CSV_DOWNLOAD_URL)

# driver.save_screenshot('selenium_screenshot.png') # 브라우저 스크린샷 
# ele = driver.find_element(By.ID, 'query') #ID값을 이용해 요소 찾기 
base_element = driver.find_element(By.XPATH, "//th[contains(text(), '令和5年7月31日')]") #ID값을 이용해 요소 찾기 
base_element.find_element(By.XPATH, "following-sibling::*[1]/a").click()
# print(ele)

# time.sleep(3)

# print(ele.get_attribute('type')) # 속성값 가져오기ㄹ 
# ele.send_keys('jongin') # 내용 입력 
# # ele.clear() # 입력한 내용 클리어 
# ele.send_keys(Keys.ENTER) #엔터키를 누르는것과 동일

driver.quit()  # 브라우저 자체 종료