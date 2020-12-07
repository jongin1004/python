#def내 에서는 밖에 있는 변수 gun 을 사용할 수 없다.
#def 안에서 다시 재설정 해줘야 그 때부터 gun 변수 사용 가능
#def 안에서 gun - soldiers를 했지만, print로 gun을 출력을 하면
#gun은 그대로 10이 남아 있게 된다.
gun = 10

def checkpoint(soldiers) :
    gun = 20 #gun 을 다시 설정안하면 오류가 뜬다.
    gun = gun - soldiers
    print(" 함수 내 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))


#####################################

gun = 10

def checkpoint(soldiers) :
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print(" 함수 내 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

#################################################
#전역변수를 많이쓰면 코드관리가 어려워 진다.  권장 x
#파라미터로 전달해서 ruturn 받는 형식으로 많이 한다.

def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print(" 함수 내 남은 총 : {0}".format(gun))
    return gun

checkpoint_ret(10, 2)
