import time
from selenium import webdriver

browser = webdriver.Chrome()


# 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭'
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("bill1224")
browser.find_element_by_id("pw").send_keys("cldhjwld")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
browser.find_element_by_id("id").clear()  # 기존에 적혀있는 id 초기화
browser.find_element_by_id("id").send_keys("my_id")


# 6.html 정보 출력
print(browser.page_source)  # 현재 페이지의 모든 html 태그를 가져온다

# 7. 브라우저 종료
# browser.close() #현재 브라우저 종료
browser.quit()  # 전체 브라우저 종료
