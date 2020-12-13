import requests

# res = requests.get("http://naver.com")
# res = requests.get("http://bill1224.tistory.com")

# print("응답코드 : ", res.status_code)  # 200이면 정상

# # requests.codes.ok  = 응답코드 200
# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# # 스크립트를 하기위해서 올바로 html문서를 갖겨왔다! 맞으면  ol 아니면 오류
# res.raise_for_status()
# print("웹 스크래핑을 진행합니다. ")


# 위의 긴 코딩을 간단하게 이 2줄로 코딩을 하면된다.
res = requests.get("http://google.com")
res.raise_for_status()
# 가져온 html 문서의 글자 갯수를 가져온다.
print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
