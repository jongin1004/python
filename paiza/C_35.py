input_line = input()
count = 0
for i in range(int(input_line)) :
    input_t = input().split(" ")
    check = input_t[0]
    del input_t[0]
    input_t = list(map(int, input_t))
    total = sum(input_t)

    if total >= 350 :
        if check == "s" :
            result = int(input_t[1]) + int(input_t[2])
            if result >= 160 :
                count += 1

        elif check == "l" :
            result = int(input_t[3]) + int(input_t[4])
            if result >= 160 :
                count += 1
print(count)

# if문을 다 밖으로 빼는 것이 좋다
student_count = int(input())
result_count = 0

for i in range(student_count):
    student_scores = input().split(" ")
    student_subject = student_scores[0]
    student_scores = list(map(int, student_scores[1:6]))

    if sum(student_scores) < 350:
        continue

    if student_subject == 's':
        sum_subject = sum(student_scores[1:3])

    if student_subject == 'l':
        sum_subject = sum(student_scores[3:5])

    if sum_subject >= 160:
        result_count += 1
print(result_count)
