import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() 
driver.get('https://www.w3schools.com')

driver.find_element(By.XPATH, "//a[text()='Learn HTML']").click()
driver.find_element(By.XPATH, "//a[text()='HOW TO']").click()
driver.find_element(By.XPATH, "//a[text()='Contact Form']").click()

fname = driver.find_element(By.ID, "fname")
lname = driver.find_element(By.ID, "lname")
country = driver.find_element(By.ID, "country")
subject = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea')

fname.send_keys('jongin')
lname.send_keys('choi')
country.send_keys('korea')
subject.send_keys('learn about selenium using python')

time.sleep(3)
# driver.save_screenshot('selenium_screenshot.png') # 브라우저 스크린샷 
# ele = driver.find_element(By.ID, 'query') #ID값을 이용해 요소 찾기 

# print(ele.get_attribute('type')) # 속성값 가져오기ㄹ 
# ele.send_keys('jongin') # 내용 입력 
# # ele.clear() # 입력한 내용 클리어 
# ele.send_keys(Keys.ENTER) #엔터키를 누르는것과 동일

driver.quit()  # 브라우저 자체 종료