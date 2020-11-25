letters = "python"
print(letters[0],letters[2])

#여러글자를 가져오는 것 = 슬라이""
#시작 인덱스를 생략하면 0으로 간주 , 끝 인덱스를 생략하면 문자열의 끝을 의미
license_plate= "24가 2210"
print(license_plate[-4:])
#슬라이싱 할 때 시작인덱스:끝인덱스:오프셋 을 지정가능
string = "HLHLHL"
print(string[::2])

string = "PYTHON"
print(string[::-1])
#replace() 특정 문자를 다른 문자로 변환
phone = "010-1234-5678"
print(phone.replace("-"," "))
print(phone.replace("-",""))
#split() 특정 문자를 기준으로 분리해서 배열형태로 만듦
url = "http://sharebook.kr"
split = url.split(".")
print(split[1])

#string은 기존 그대로 출력이된다. 문자열은 변경할 수 없는 자료형이기 때문에
#relace를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해준다.
string = 'absdf'
string.replace('a','A')
print(string)
print(string.replace('a','A'))
