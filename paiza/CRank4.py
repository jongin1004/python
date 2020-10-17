input_line = input()
check = input_line.split(" ")
count = int(check[0])
input_t = [0 for _ in range(count)]
for i in range(0,count) :
    input_t[i] = input()

for j in range(0, count) :
    score_check = input_t[j].split(" ")
    result = int(score_check[0]) - int(score_check[1])*5
    if result < 0 :
        result = 0
    if result >= int(check[1]) :
        print(j+1)
