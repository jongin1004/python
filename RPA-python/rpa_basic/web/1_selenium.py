from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_driver_path = "/Users/jongin/project/python/RPA-python/rpa_basic/web/chromedriver"  # 다운로드한 ChromeDriver의 경로로 변경해야 합니다.
# service = webdriver.chrome.service.Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome() # 인자를 생략하면, 자동적으로 동일한 path에서 드라이버를 찾음 

driver.get('https://naver.com')

driver.save_screenshot('selenium_screenshot.png') # 브라우저 스크린샷 
ele = driver.find_element(By.ID, 'query') #ID값을 이용해 요소 찾기 

print(ele.get_attribute('type')) # 속성값 가져오기ㄹ 
ele.send_keys('jongin') # 내용 입력 
# ele.clear() # 입력한 내용 클리어 
ele.send_keys(Keys.ENTER) #엔터키를 누르는것과 동일

driver.close() # 현재 탭만 종료
driver.quit()  # 브라우저 자체 종료