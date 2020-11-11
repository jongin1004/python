def make_url(url) :
    return "www."+url+".com"

print(make_url("naver"))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def make_list(str) :
    str_list = []
    for i in str :
        str_list.append(i)

    return str_list

print(make_list("abcd"))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def pickup_even(num_list) :
    result = []
    for i in num_list :
        if i % 2 == 0 :
            result.append(i)

    return result

print(pickup_even([3, 4, 5, 6, 7, 8]))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def convert_int(type_str) :
    type_str = type_str.split(",")
    type_str = "".join(type_str)
    return int(type_str)

print(type(convert_int("1,234,567")), convert_int("1,234,567"))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def convert_int2(type_str) :
    return int(type_str.replace(',', ''))

print(type(convert_int2("1,234,567")),convert_int2("1,234,567"))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
