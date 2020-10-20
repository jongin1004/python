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
