test_list = [1,2,3,4,5,6,7,8]

try :
    for num in test_list :
        if num%3 == 0 :
            raise Exception("ss")
        print(num)

except Exception as e :
    print("aaa", e)


####################################

def find_three_multiple():
    for num in test_list :
        if num % 3 == 0:
            raise Exception('num :' + str(num))    # num이 3의 배수일 때 ,예외를 발생시킴
        print(num)                                    # 현재 함수 안에는 except가 없으므로
                                                      # 예외를 상위 코드 블록으로 넘김

try:
    find_three_multiple()
except Exception as e:                             # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('existing three find_three_multiple ', e)

###############################################

def find_three_multiple():
    try:
        for num in test_list :
            if num % 3 == 0:
                raise Exception('num :' + str(num))    # num이 3의 배수일 경우,예외를 발생시킴
            print(num)
    except Exception as e:                             # 함수 안에서 예외를 처리함
        print('exception generation in find_three_multiple .', e)
        raise    # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김

try:
    find_three_multiple()
except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('exception generation in script', e)
