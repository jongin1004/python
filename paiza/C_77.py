input_line = input().split(" ")
distribution = 100/int(input_line[1])
for i in range(int(input_line[0])):
    input_t = input().split(" ")
    date = int(input_t[0])
    answer_count = int(input_t[1])

    if date <= 0 :
        result = distribution*answer_count

    elif date >= 10 :
        result = 0

    else :
        result = (distribution*answer_count)*0.8


    if result >= 80 :
        print("A")

    elif result >=70 and result < 80 :
        print("B")

    elif result >= 60 and result < 70 :
        print("C")

    else :
        print("D")
