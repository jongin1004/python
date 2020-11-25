# 기본적으로 데이터 언패킹은 좌변의 변수와 우변의 데이터 개수가 같아한다.
# *를 사용하면 개수가 달라도 데이터 언패킹을 할 수가 있다.
scores = [8.8, 8.9, 9.2, 9.9, 9.5, 9.4]
*valid_score, _,_ = scores
print(valid_score)
_, _,*valid_score2 = scores
print(valid_score2)


#딕셔너리 만들기
temp = {}

ice = {"merona" :1000, "polrapo" :1200, "bbang":1800}
print(ice)

ice["zzyosuba"] = 1200
ice["worldcon"] = 1500
print(ice)

print("merona price :" + str(ice["merona"]))

ice["merona"] = 1300
print(ice)

del ice["merona"]
print(ice)
