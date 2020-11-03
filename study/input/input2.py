# input_str = input("문자 한개를 적어주세요. :")
# if input_str.islower() :
#     print(input_str.upper())
# else :
#     print(input_str.lower())

# input_score = input("성적 입력 :")
# score = int(input_score)
# if score <= 100 and score >= 81 :
#     print("A")
# elif score <= 80 and score >= 61 :
#     print("B")
# elif score <= 60 and score >= 41 :
#     print("C")
# elif score <= 40 and score >= 21 :
#     print("D")
# else :
#     print("F")

# input_number1 = int(input("Number 1 :"))
# input_number2 = int(input("Number 2 :"))
# input_number3 = int(input("Number 3 :"))
# print(max(input_number1, input_number2, input_number3))

tongsinsa = {"011" : "SKT", "016" : "KT", "019" : "LGU", "010" : "NONE"}
input_number = input("번호 입려해주세요")
check = input_number[:2]
print(tongsinsa[check])


우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")


주민번호 = input("주민등록번호: ")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")





import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

range_of_fluctuation = int(btc["max_price"]) - int(btc["min_price"])
if (int(btc["opening_price"]) + range_of_fluctuation) > int(btc["max_price"]) :
    print("up")

else :
    print("down")
