from random import *

count = 0

for i in range(50) :
    a = randint(5,50)
    if a >= 5 and a <= 15 :
        print("[o] {0}번째 손님 (소요시간 : {1}분".format(i,a))
        count += 1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i,a))

print("총 탑승 승객 : {0} 분".format(count))
