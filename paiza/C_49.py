#49번
input_line = input()
input_t = [1 for _ in range(int(input_line)+1)]
for a in range(1,int(input_line)+1) :
    input_t[a] = input()

total = 0
for b in range(0, int(input_line)) :
    result = int(input_t[b]) - int(input_t[b+1])
    if result > 0 :
        total += result
    else :
        total += -result
print(total)
