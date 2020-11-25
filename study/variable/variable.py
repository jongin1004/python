삼성전자 = 50000
보유주식주 = 10
총평가금액 = 삼성전자*보유주식주
print(총평가금액)

시가총액 = 29800000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))

s = "hello"
t = "python"
print(s+"!",t)
#type()는 변수의 data tpye를 알려준다.
a = "132"
b = 132
print(type(a))
print(type(b))
#int() 를 사용하면 해당 변수를 int type으로 변환
num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int))

num= 100
num_str = str(num)
print(num_str,type(num_str))

num_str = "15.79"
num_float = float(num_str)
print(num_float, type(num_float))

year = "2020"
year_int = int(year)
print(year_int,year_int-1,year_int-2)

price = 48584
month = 36
total = price * month
print(total)
