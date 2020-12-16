import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
# newline을 공백으로 안해주면 자동으로 줄바꿈이 남
f = open(filename, "w", encoding="utf-8-sig", newline="")
# newline="" 리스트마다 줄바꿈되는것을 막는다
# utf-8-sig 엑셀파일에서 한글이 깨지는 것을 막기 위함
writer = csv.writer(f)

res2 = requests.get(
    "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1")
# res2.raise_for_status()
# soup2 = BeautifulSoup(res2.text, "lxml")

# titles = soup2.find("table", attrs={"class": "type_2"})\
#     .find("thead").find_all("th")

# title = [title.get_text().strip() for title in titles]
# writer.writerow(title)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"})\
        .find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 의미 없는 데이터 스킵
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)  # list형태로 집어넣는다.
