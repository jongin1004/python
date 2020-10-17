input_line = input()
input_t = [1,2,3,4,5,6,7]
count = 0
for a in range(0, int(input_line)+1) :
    input_t[a] = input()


for b in range(1,int(input_line)+1) :
    result = input_t[b].find(input_t[0])
    if result != -1 :
        count += 1
        print(input_t[b])

if count == 0:
    print("None")
