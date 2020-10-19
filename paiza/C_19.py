input_line = input()
aliquot = []
for i in range(int(input_line)) :
    input_t = input()

    for j in range(1, int(input_t)+1) :
        if int(input_t)%j == 0 :
           aliquot.append(j)

    aliquot.remove(int(input_t))

    if sum(aliquot) == int(input_t) :
        print("perfect")
    elif (int(input_t)-sum(aliquot)) == 1 or (int(input_t)-sum(aliquot)) == -1 :
        print("nearly")
    else :
        print("neither")
    aliquot = []
