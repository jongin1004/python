input_line = input()
count = int(input_line)
input_t = [0 for _ in range(count)]
var =  [0 for _ in range(count)]
sub = 0
add = 0
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
        add = int(input_t[i][1])
        result = set1 + add
    elif check == "SUB" :
        sub = int(input_t[i][1])
        result = set1 - sub
