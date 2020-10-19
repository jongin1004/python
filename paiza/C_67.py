import math

input_line = input()
Binary = []
count = 0
run = True
check = input_line.split(" ")
input_t = [0 for _ in range(int(check[0]))]
for i in range(int(check[0])) :
    input_t[i] = input()

result = int(check[1])
while  run :
    Binary.append(result%2)
    result = math.floor(result/2)
    if result <= 1 :
        run = False

Binary.append(1)
for a in range(int(check[0])) :
    print(Binary[int(input_t[a])-1])


input_line = input().split()
count = int(input_line[0])
number = int(input_line[1])
two_jinsu_arrays = []

while (number >= 1):
    two_jinsu_arrays.append(number % 2)
    number = number // 2

for i in range(count):
    index = int(input())
    print(two_jinsu_arrays[index - 1] )
