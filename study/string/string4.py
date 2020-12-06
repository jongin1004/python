python = "Python is Amazing"
print(python[0].isupper()) #[]인덱스가 대문자인지 확인
print(python[1].islower()) #[]인덱스가 소문자인지 확인

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("e")) #find는 원하는 값이 없으면 -1을 출력
# print(python.index("e")) #index는 원하는 값이 없으면 오류


#포멧팅

print("i'm %d" % 20) # d 는 정수
print("i like %s" % "python") # s 는 문자열,정수 모두 가능
print("Apple is started by %c." % "A") #c 는 한 글자(문자)
print("aaa %s sss %s" %("blue", "red"))

print("aaa {}".format(20))
print("aaa {0} sss {1}".format("blue", "red"))
print("aaa {1} sss {0}".format("blue", "red"))

print("aaa {age}, sss{color}".format(age = 20, color = "red"))
print("aaa {color}, sss{age}".format(age = 20, color = "red"))

age = 20
color = "red"
print(f"aaa {color}, sss{age}") #f를 앞에 적게되면 {}안에 실제 변수이름 을 적어주면 그것이 그대로 적용


######################################
#탈출문자
print("Red Apple\rPine") #\r 커서를 맨 앞으로 이동
print("Red Apple\bPine") #\b 백스페이스 (한 글자 삭제)


#######################################

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
print(f"password of {url} is {password}")
