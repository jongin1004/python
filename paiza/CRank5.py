input_line = input()
count = int(input_line)
input_t = [0 for _ in range(count)]
for i in range(0, count) :
    input_t[i] = input()
    input_t[i] = input_t[i].split(" ")
    check = input_t[i][0]
    if check == "SET" :
        if input_t[i][1] == "1" :
            set1 = int(input_t[i][2])
        else :
            set2 = int(input_t[i][2])
    elif check == "ADD" :
        set2 = set1 + int(input_t[i][1])
    elif check == "SUB" :
        set2 = set1 - int(input_t[i][1])

print(set1, result)

input_line = input()
count = int(input_line)
set1 = 0
set2 = 0
for i in range(0, count) :

    input_t = input().split(" ")

    if input_t[0] == "ADD":
        set2 = set1 + int(input_t[1])
        continue
    if input_t[0] == "SUB":
        set2 = set1 - int(input_t[1])
        continue
    if input_t[1] == "1":
        set1 = int(input_t[2])
    else:
        set2 = int(input_t[2])

print(set1, set2)
