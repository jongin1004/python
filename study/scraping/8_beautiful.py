import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=648419&weekday=mon"
res = requests.get(url)
res.raise_for_status()  # 문제있을 경우 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class": "title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# 만화 제목과 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com"+cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    # 최근 만화 10개에 대한 평균 평점
    total_rates += float(rate)  # 지금 평점은 sting상태라서
print("점체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))
