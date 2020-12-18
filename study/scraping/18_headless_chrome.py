import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# 크롬이 없는 크롬, 크롬을 뛰우지않고 사용할 수 있다. 백그라운드에서 동작
# 빠른 선능으로 브러우저를 뛰우지 않고도 동작한다.
# 브라우저를 뛰워서 동작하면 메모리도 많이 잡아먹고 속도도 느리다.
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")


browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

interval = 2  # 2초에 한번씩 스크롤을 내릴거다

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
# 스크린샷 저장
browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": ["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())  # html 문서를 예쁘게 출력

for movie in movies:

    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "할인되지 않은 영화 제외")
        continue

    # 할인된 가격
    price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    # https://play.google.com + link로 해야 올바른 링크가 된다.

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : https://play.google.com" + link)
    print("-"*120)

browser.quit()
