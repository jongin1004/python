import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=5&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class": "name"}).get_text())
for item in items:
    # 무료배송인 것 만 보고싶을 경우
    delivery_type = item.find(
        "span", attrs={"class": re.compile("^badge badge-delivery")})
    if delivery_type:
        print("무료배송")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()

    # 애플 제품 제외
    if "Apple" in name:
        print("애플 상품 제외")
        continue

    price = item.find("strong", attrs={"class": "price-value"}).get_text()

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class": "rating"})
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외합니다>")

    rate_cnt = item.find(
        "span", attrs={"class": "rating-total-count"})

    if rate_cnt:
        rate_cnt = rate_cnt.get_text()  # (26)
        rate_cnt = int(rate_cnt[1:-1])
    else:
        print(" <평점 수 없는 상품 제외합니다>")

    if float(rate) >= 4.5 and rate_cnt >= 100:
        print(name, price, rate, rate_cnt)
