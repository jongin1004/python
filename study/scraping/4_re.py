# 정규식 : 정해진 형태를 의미하는 식
import re
# 주민등록번호
# 901201-1111111

# 이메일 주소
# nadocoding@gmail.com

# 차량 번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1

# 위에 것들은 저마다의 정해진 형태가 있다.

# ca?e 4개의 문자중에 3개 밖에 생각이 나지 않느 상황
# 경우에 수는 caae, cabe, ... 등 여러가지  이럴 때 정규식을 사용

p = re.compile("ca.e")
# . (ca.e): 하나의 문자를 의미   care, cafe (o) |  caffe는 (x)
# ^ (^de) : 문자열의 시작을 의미, de로 시작하는 문자열  desk, destination (o) | fade(x)
# $ (se$) : 문자열의 끝  case, base (o) | face (x)

# p 의 정규식과 비교하기 위해서 match를 사용
m = p.match("case")
# print(m.group())  # 정규식과 match가 되지 않으면 오류가 난다.


def print_match(m):
    # 이렇게 사용하면 오류가 나지 않고 계속 프로그램을 사용할 수 있다.
    if m:
        print("m.group() :", m.group())  # 일치하는 문자열 반환
        print("m.string :", m.string)  # 입력받은 문자열 반환
        print("m.start :", m.start())  # 일치하는 문자열의 시작 index
        print("m.end :", m.end())  # 일치하는 문자열의 끝 index
        print("m.span :", m.span())  # 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음 ")


# m = p.match("careless")
# match : 주어진 문자열의 처음부터 일치하는지 확인, 뒤에는 뭐가 오든 상관없음
# print_match(m)

# m = p.search("good care")  # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("cafe2care")  # findall : 일치하는 모든 것을 리시트 형태로 반환
# print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열 ") :주어진 문자열의 처음부터 일치하는지 확인, 뒤에는 뭐가 오든 상관없음
# 3. m = p.search("비교할 문자열"): 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리시트 형태로 반환

# 원하는 형태 :정규식
# . (ca.e): 하나의 문자를 의미   care, cafe (o) |  caffe는 (x)
# ^ (^de) : 문자열의 시작을 의미, de로 시작하는 문자열  desk, destination (o) | fade(x)
# $ (se$) : 문자열의 끝  case, base (o) | face (x)

# w3school.com  -> python -> RegEx 가면 정규식에 관한 내용을 더 볼 수 있다.
# 또는 python re 를 검색해서 들어가면 공식 python에서 볼 수 있음
