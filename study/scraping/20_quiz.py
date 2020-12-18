# 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# [조회조건]

# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ========== 매물 1 ==========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,00 (만원)
# 동 : 214동
# 층 : 고/23

# ======== 매물 2 =============

# slenuum 사용해서 풀기
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

url = "http://daum.net"
browser.get(url)

elem = browser.find_element_by_id("q")
elem.send_keys("송파 헬리오시티")

elem = browser.find_element_by_xpath(
    "//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()

soup = BeautifulSoup(browser.page_source, "lxml")

info = soup.find("table", attrs={"class": "tbl"}).find("tbody").find_all("tr")

for idx, text in enumerate(info):

    columns = text.find_all("td")
    print(f"========== 매물 {idx} ==========")
    print(f"거래 : {columns[0].get_text()}")
    print(f"면적 : {columns[1].get_text()} (공급/전용)")
    print(f"가격 : {columns[2].get_text()} (만원)")
    print(f"동 : {columns[3].get_text()}")
    print(f"층 : {columns[4].get_text()}")

browser.quit()


##########################################
#requests로 풀기 

# url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# header를 User-Agent를 사용해야하는지 아니면, 잘 받아오고 있는지
# 확이하기 위해서 prettify()를 사용해서 확인
# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

# data_rows = soup.find("table", attrs={"class": "tbl"}).find(
#     "tbody").find_all("tr")
# for idx, row in enumerate(data_rows):
#     columns = row.find_all("td")

#     print(f"========== 매물 {idx} ==========")
#     print(f"거래 : {columns[0].get_text().strip()}")
#     print(f"면적 : {columns[1].get_text().strip()} (공급/전용)")
#     print(f"가격 : {columns[2].get_text().strip()} (만원)")
#     print(f"동 : {columns[3].get_text().strip()}")
#     print(f"층 : {columns[4].get_text().strip()}")
