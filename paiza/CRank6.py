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
