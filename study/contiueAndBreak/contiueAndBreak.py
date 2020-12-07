absent = [2,5]
no_book = [3]
#continue는 현재 루프를 더이상 진행하지 않고 다음 루프로 진행하도록
#break가 나오면 더 이상 루프를 진행하지 않고 아예 종료
for student in range(1,11) :
    if student in absent :
        continue
    elif student in no_book :
        print("end, come on {0}".format(student))
        break
    print("{0}, hi".format(student))
