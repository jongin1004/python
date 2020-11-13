def print_reverse(str) :
    print(str[::-1])

print_reverse("python")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def print_even(num_list) :
    print(num_list[::2])

print_even ([1, 3, 2, 10, 12, 11, 15])

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def print_even2(num_list) :
    for num in num_list :
        if num % 2 == 0 :
            print(num)

print_even2 ([1, 3, 2, 10, 12, 11, 15])

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def print_keys(my_dict) :
    for key in my_dict :
        print(key)

print_keys ({"name":"leema", "year":30, "zender":0})

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(my_dict, date) :
    print(my_dict[date])

print_value_by_key  (my_dict, "10/26")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

import math

string = "pythonrubytest"
count = math.ceil(len(string)/5)
def print_5xn(str) :
    num = 0
    for i in range(count) :
        print(str[num:num+5])
        num += 5

print_5xn(string)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

string = "pythonrubytest"
def print_5xn(str,str_num) :
    num = 0
    count = math.ceil(len(str)/str_num)
    for i in range(count) :
        print(str[num:num+str_num])
        num += str_num

print_5xn(string,3)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
