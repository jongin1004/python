inventory = {"merona":[300,20],
             "bibibic":[400,3],
             "zzyosuba":[250,100]}
print(inventory)
print(inventory["merona"][0],"won")

inventory["worldcon"] = [500,7]
print(inventory)
#keys() 딕셔너리에서 keys값만 출력하도록
icecream = {'tank': 1200, "polrapo":1200,"bbang":1800,"worldcon":1500}
ice = list(icecream.keys())
print(ice)
#values() 딕셔너리에서 values 값만 출력하도록
ice2 = list(icecream.values())
print(ice2)

print(sum(icecream.values()))

new_product = {"qwer":2700, "asdf":1000}
icecream.update(new_product)
print(icecream)
# zip 과 dict 두개의 튜플을 하나의 딕셔너리로 변환
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
