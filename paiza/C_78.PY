#78번
input_line = input()
info = input_line.split()
# input_t = [0 for _ in range(int(info[0]))]
count = 0
money = 0
for i in range(int(info[0])) :
    input_t = input()
    if i+1 != int(info[0]) :
        if int(input_t) <= int(info[1])  :
            count += 1
            money -= int(input_t)

        if int(input_t) >= int(info[2])  :
            money += int(input_t)*count
            count = 0

    else :
        money += int(input_t)*count
        count = 0
        break

print(money)
