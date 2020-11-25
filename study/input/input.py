# user = input("입력 : ")
# print(user * 2)
#
# input_num = input("숫자를 입력하세요 : ")
# print(int(input_num)+10)

# input_num = input("숫자를 입력하세요 : ")
# num_check = int(input_num)%2
# if num_check == 0 :
#     print("jjack")
# else:
#     print("hole")

# input_num = input("숫자를 입력하세요 : ")
# result = int(input_num) + 20
# if result > 255:
#     print("출력 값 : 255")
# else:
#     print("출력 값 : "+str(result))

# input_num = input("숫자를 입력하세요 : ")
# result = int(input_num) - 20
# if result >= 0 and result <= 255:
#     print(result)
# elif result < 0:
#     print(0)
# else:
#     print(255)

# input_h = input("현재 몇 시 :")
# input_m = input("현재 몇 분 :")
# total_m = int(input_h)*60 + int(input_m)
# if total_m%60 == 0:
#     print("정각입니다.")
# else :
#     print("정각이 아닙니다.")

# fruit = ["사과", "포도", "홍시"]
# input_fruit = input("좋아하는 과일은? :")
# if input_fruit in fruit:
#     print("정답입니다.")
# else:
#   print("오답입니다.")

# warn_inverstment_list = ["Google", "Naver", "kakao"]
# input_investment = input("투자 종목을 입력 하세요 : ")
# if input_investment in warn_inverstment_list :
#     print("투자 경고 종목o.")
# else:
#     print("투자 경고 종목 x.")

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가좋아하는계절은: ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
