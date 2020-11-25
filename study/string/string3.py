#upper() 소문자를 대문자로 바꿔줌
ticker = "btc_krw"
print(ticker.upper())
#lower() 대문자를 소문자로 바꿔줌
ticker = "BTC_KRW"
print(ticker.lower())
#capitalize() 대문자로 만들어줌
string = "hello"
print(string.capitalize())
#endswith() 뒷 문자열이포함 된 경우 true 미포함된 경우 false
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
# xlsx 또는 xls이 포함된 것을 확인할 때는 ","를 통해서 하면 된다.
print(file_name.endswith(("xlsx","xls")))
#startswith() 앞 문자열이 포함 된 경우 true 미포함 된 경우 false
file_name = "2020_asd.xlsx"
print(file_name.startswith("2020"))

a = "hello world"
a_array = a.split(" ")
print(a_array)

data = "04142     "
print(data.rstrip())
