from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)  # url로 이동

# 가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달 달력
# browser.find_elements_by_link_text("28")[0].click()  # [0] -> 이번달 달력

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click()  # [0] -> 다음달 달력
# browser.find_elements_by_link_text("28")[1].click()  # [0] -> 다음달 달력


# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달 달력
browser.find_elements_by_link_text("28")[1].click()  # [0] -> 이번달 달력


# 제주도 선택
browser.find_element_by_xpath(
    "//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# time.sleep(3) #검색하고 나서 로딩이 있기 때문에, 바로 가져올 수가 없기 때문에 offset을 준다
# sleep보다 더 좋은, 이 element가 나올 때까지 기달려! 라는 설정을 할 수 있다.
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행
    print(elem.text)  # 첫번째 결과 출력
finally:
    # 동작 수행이 끝나거나, 오류났을 경우에는 browser 종료
    browser.quit()
# browser를 10초까지 기달린다. 어떤 것을?? XPath란 조건으로 //*[@id='content']/div[2]/div/div[4]/ul/li[1]값이 해당하는
# element값을 기달려라 라는 의미다
# XPATH 이외에도 ID, CLASS_NAME, LINK_TEXT 등 사용가능

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath(
#     "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)  # elem의 text값
