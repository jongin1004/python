def print_coin():
    print("bitcoin")

for i in range(100) :
    print_coin()

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def print_coins():
    for i in range(100) :
        print("bitcoin")

print_coins()

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def message1(str) :
    print(str)

message1("Hi")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def print_with_smile(str) :
    print(str+":D")

print_with_smile("jongin")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def print_max(a,b,c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

print_max(2,7,3)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
