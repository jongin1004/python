import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()  # 문제있을 경우 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")
# # 가져온 html 문서를 lxml파서를 통해서 beautifulsoup객체로 만든 것

# print(soup.title) #title의 전체 태그를 스크랩핑
# print(soup.title.get_text()) #title 태그의 원소값만 스크랩핑
# print(soup.a) # 스크랩핑 해온 html에서 맨 처음 나오는 a element를 가져와
# print(soup.a.attrs)  # a element 의 속성 정보를 가져옮
# print(soup.a["href"])  # a element 의 href 속성에 대한 값만 가져옮

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# # find는 뒤에 조건에 해당되는 것들 중에서 맨 처음에 있는 것을 가져온다.
# # class": "Nbtn_upload 인 a element
# print(soup.find(attrs={"class": "Nbtn_upload"}))
# # class": "Nbtn_upload가 중복되는게 없다면, 태그도 생략가능하다.

# print(soup.find("li", attrs={"class": "rank01"}))

rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text)
# rank2 = rank1.next_sibling.next_sibling #next_sibling : 다음 태그로 넘어가는 것
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling #previous_sibling : 이전 태그로 돌아가는 것
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")  # next_sibling하는데 조건에 맞는 것만 찾는다.
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))  # rank1기준으로 조건에 맞는 모든 형제 태그들을 가져온다

webtoon = soup.find("a", text="사신소년-76화 급습")
print(webtoon)
