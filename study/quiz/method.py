#표준 체중을 구하는 프로그램을 작성해라

#성별에 따른 공식
# 남자 : 키 (m) x 키 (m) x 22
# 여자 : 키 (m) x 키 (m) x 21

#조건1 : 표준체중은 별도의 함수 내에서 계산
# *함수명 : std_weight
# *전달값 : height, gender

#조건2 : 표준체중은 소수점 둘째자리까지 표시

#출력 예제
#키 175cm 남자의 표준 체중은 67.38kg 입니다.

####################################################

def std_weight(height, gender) :

    if gender == "m" :
        result = (height*0.01)**2 * 22
        result = round(result, 2) # 소수점 2째 짜리 까지 반올림
    else :
        result = (height*0.01)**2 * 21
        result = round(result, 2)

    print("height{0}cm {1}의 표준 체중은 {2}kg 입니다.". \
    format(height, gender, result))

std_weight(175, "m")
