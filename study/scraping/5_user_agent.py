# user-Agent를 headers 정보에 줘야지만 제대로 스크랩핑을 해올 수 있다.
# 사이트마다 다른목적으로 들어온 컴퓨터에 대한 것은 정보를 제한 하는 경우가 많기 때문에

import requests
headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = "http://nadocoding.tistory.com"
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
