# my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가

for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])

print("-----------------------------------")

# my_list = ["가", "나", "다", "라", "마"]
# 가 나 다
# 나 다 라
# 다 라 마

for i in range( 1, len(my_list) - 1 ):
    print(my_list[i-1], my_list[i], my_list[i+1])

print("-----------------------------------")
