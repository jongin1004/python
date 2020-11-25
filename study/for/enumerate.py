#enumerate() 는 index번호와 value 값을 tuple 형태로 만들어주는 역할이다.

t = [1, 5, 7, 33, 39, 52]
for p in enumerate(t):
    print(p)

# for 문과 if 문을 같이 사용할 수 있다.
new_t_list = [i for i in t if i >= 2]
print(new_t_liszt)

test_list = [i for i, x in enumerate(t) if x >= 1]
print(test_list)
