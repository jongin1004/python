i = 0
input_line = "PAIZE"
leet = {"A" : "4" , "E" : "3", "G" : "6" , "I" : "1" , "O" : "0" , "S" : "5", "Z" : "2"}
result = ""

# ver.1
if(input_line[i] in leet):
    result += leet[input_line[i]]
    continue
result += input_line[i]

#ver.2  삼항 연산자를 활용한 코딩
for i in range(len(input_line)):
    result += (leet[input_line[i]] if input_line[i] in leet else input_line[i] )
print(result)



# while i < 3 :
#     string.+i = (string.+(i-1)) + "*"
#     i = i + 1
# print(string)
#
# leet = {"A" : "4" , "E" : "3", "G" : "6" , "I" : "1" , "O" : "0" , "S" : "5", "Z" : "2"}
# input_line = input()
# i = 0
# while i < len(input_line) :
#     if "A" in input_line :
#         string[i] = input_line.replace("A","4")
# print(string)
