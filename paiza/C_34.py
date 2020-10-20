input_line = input().split(" ")
result = 0

if input_line[1] == "+" :
    if input_line[0] == "x" :
        result = int(input_line[4]) - int(input_line[2])

    elif input_line[2] == "x" :
        result = int(input_line[4]) - int(input_line[0])

    else :
        result = int(input_line[0]) + int(input_line[2])

elif input_line[1] == "-" :
    if input_line[0] == "x" :
        result = int(input_line[4]) + int(input_line[2])

    elif input_line[2] == "x" :
        result = int(input_line[0]) - int(input_line[4])

    else :
        result = int(input_line[0]) - int(input_line[2])

print(result)
