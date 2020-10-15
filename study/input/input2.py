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
