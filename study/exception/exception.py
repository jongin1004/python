# 예외처리를 이용해서 없는 파일이나 list에 없는 값을 잘몬 접근한다던지
# 그런 문제로 인해서 프로그램이 강제종료되는 것을 막을 수 있게 된다.
# 오류가 뜨게 되면 프로그램이 강제종료되기 때문에 예외처리로 그것을 막아줄 수 있음


# try 내부에 문장이 실행이되다가 문제가 발생했을 때 except 부분을 찾아서
# 문장에서 오류난 부분이 except부분에 존재가 하면  ValueError 가 있으면
# 그 내부에있는 문장을 실행하게 된다.66
try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# 에러가 발생했을 때 에러의 타입이 ValueError일 경우에 아래 문장 실행
except ValueError:
    print("에러! 잘못된 값을 입력했습니다.")
# 에러가 발생했을 때 에러의 타입이 ZeroDivisionError 경우에 아래 문장 실행
except ZeroDivisionError as err:
    print(err)
# 에러가 발생했는데 타입이 ValueError, ZeroDivisionError가 아닌 나머지일 경우에 실행
# except:
#     print("알 수 없는 에러가 발생하였습니다.")

# 에러 type은 모르고 어떤 에러가 발생했는지 문구를 보고 싶은 경우에는
except Exception as err:
    print(err)
