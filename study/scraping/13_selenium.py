# slenium은 웹페이지 테스트 자동화를 할 수 있는 유용한 프레임 워크
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Chrome()
# Chrme webdriver 객체를 생성을 하고,  그 browser에서 url로 이동하는 것
browser.get("http://naver.com")

elem = browser.find_element_by_class_name(
    "link_login")  # class 값이 link_login인 걸 찾음
elem.click()  # 클릭
browser.back()  # 전 페이지
browser.forward()  # 앞 페이지
browser.refresh()  # 페이지 새로고침
browser.back()
elem = browser.find_element_by_id("query")  # id 값이 query 인 element를 찾는다.

# 키보드의 ENTER나 여러 기능을 사용하고 싶을 경우에는 Keys를 import해와야함
elem.send_keys("나도코딩")  # 데이터(글자)를 보내기만 하는 경우에는 Keys import가 필요없음
elem.send_keys(Keys.ENTER)


elem = browesr.find_elements_by_tag_name("a")
# elements 는  조건에 맞는 모든 elemet를 가져오라는 뜻
# a 태그인 element를 모두 가져와라
for e in elem:  # a 태그의 element에서 href의 속성 값만 가져오고 싶을 때
    e.get_attribute("href")


browser.get("http://daum.net")
elem = browser.find_element_by_name("q")  # 주소창에 해당하는 name 속성의 값이 q 인 것을 지목


elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
browser.back()
elem.send_keys("나도코딩")


elem = browser.find_element_by_name("q")  # 주소창
elem.send_keys("나도코딩")  # 주소창에 "나도코딩" 입력
elem = browser.find_element_by_xpath(
    "//*[@id='daumSearch']/fieldset/div/div/button[2]")
# xpath를 이용해서 검색창의 검색 링크부분을 지목한다.

elem.click()  # 검색 링크를 클릭
browser.close()  # 현제 브라우저만 닫기
browser.quit()  # 전체 브라우저 닫기
