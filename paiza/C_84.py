#84번
input_line = input()
len = len(input_line)
i = 0
string = ""
while i < len+2 :
    string += "+"
    i += 1
print(string)
print("+" + input_line + "+")
print(string)

#최대한 리펙토링
input_line = input()
string = ""
for i in range(0,len(input_line)+2) :
    string += "+"
print(string + "\n+" +
input_line + "+\n" + string)
