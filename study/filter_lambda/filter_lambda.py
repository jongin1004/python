input_food = ["banana", "kimchi", "melon", "fasd", "melon"]

new_list = list(filter(lambda x: input_food[x] == "melon", range(len(input_food))))
print(new_list)

int_list = [-2,-1,0,5,8]
new_list = list(filter(lambda x : x > 0, range(len(int_list))))
print(new_list)
