#51번
input_line = input()
num = input_line.split()
num_box = ""
for i in range(len(num)-1):
    for j in range(len(num)-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

result = int(num[3]+num[0]) + int(num[2]+num[1])
print(result)
