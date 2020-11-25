a = "3"
b = "4"
print(a+b)

print("Hi"*3)

print("-"*80)

t1 = "python"
t2 = "java"
print((t1+" "+t2+" ")*3)

# formatting %s 는 문자열 데이터 값을 %d는 정수형 데이터 타입 값을 출력
name1 = "jongin"
age1 = 10
name2 = "leema"
age2 = 13
print("name : %s age : %d" %(name1, age1))
print("name : %s age : %d" %(name2, age2))
#format() 을 사용해도 % formatting과 비슷하다.
print("name : {} age : {}".format(name1,age1))
#f-string는 좀더 편리하게 사용할 수 있다.
print(f"name : {name1} age : {age1}")

상장주식수 = "5,969,782,550"
상장주식수2 = 상장주식수.replace(",","")
상장주식수3 = int(상장주식수2)
print(상장주식수3)

분기 = "2020/03(E) (IFRS연결)"
슬라이싱 = 분기[:10]
print(슬라이싱)

data = "   hello   "
print(data.strip())
