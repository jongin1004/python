from random import *
# list = [1,2,3,4,5]
# print(list)
# shuffle(list) #list 순서를 랜덤으로 바꿈
# print(list)
# print(sample(list,1)) #list중에서 1개를 무작위로 뽑겠.



users = list(range(1,21))
shuffle(users)
print(users)

winners = sample(users, 4)

print(" ---aaaa----")
print("aaa : {0}".format(winners[0]))
print("bbb : {0}".format(winners[1:]))
print("------------")
