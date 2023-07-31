import time
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

encoded_username = quote('jongin')
encoded_password = quote('7Hp!*S5RaWd')

driver.get(f'https://{encoded_username}:{encoded_password}@netreal.jp/admin')

time.sleep(10)

# ele = driver.find_element(By.ID, 'search')
# print(ele)
# ele.send_keys('jongin')
# ele.send_keys(Keys.ENTER)

# driver.execute_script('window.scrollTo(0, 1080)')

# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# interval = 2
# prev_height = driver.execute_script('return document.body.scrollHeight')
# print(prev_height)

# time.sleep(5)

driver.quit()