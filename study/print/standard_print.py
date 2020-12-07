print("python", "java")
print("python" + "java")
#sep = 구분되는 두 문자열 사이에 특정 문자열을 삽입할 때
#end print는 원래 마지막에 줄바꿈이 자동적으로 되지만
#end를 사용하면 줄바꿈 대신의 문자열을 추가해줄 수 있음
# => 줄바꿈이 일어나지 않음
print("python", "java", "js", sep=",", end=" ? ")
print("select")


###########################################
import sys

#stdout는 표준 출력으로 문장이 찍힌다
#stderr는 표준 에로로  처리
#stderr는 에러를 확인해서 수정해야할 때
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)

############################################
#시험 성정
scores = {"a" : 0, "b" :50, "c" : 100}
for subject, score in scores.items():
    # print(subject, score)

    #ljust(a) 왼쪽정렬 a칸 수 만큼
    print(subject.ljust(8), str(score).rjust(4), sep =":")

#은행 대기순번표
#001, 002,003.....
for num in range(20):
    #zfill(a) a자리수 만큼 0으로 빈자리를 채운다.
    print("대기번호 : " + str(num).zfill(3))
