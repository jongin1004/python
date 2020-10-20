input_line = input().split(" ")

if input_line[1] == "+" :
    if input_line[0] == "x" :
        input_line[0] = int(input_line[4]) - int(input_line[2])
        print(input_line[0])

    elif input_line[2] == "x" :
        input_line[2] = int(input_line[4]) - int(input_line[0])
        print(input_line[2])

    else :
        input_line[4] = int(input_line[0]) + int(input_line[2])
        print(input_line[4])

elif input_line[1] == "-" :
    if input_line[0] == "x" :
        input_line[0] = int(input_line[4]) + int(input_line[2])
        print(input_line[0])

    elif input_line[2] == "x" :
        input_line[2] = int(input_line[0]) - int(input_line[4])
        print(input_line[2])

    else :
        input_line[4] = int(input_line[0]) - int(input_line[2])
        print(input_line[4])
