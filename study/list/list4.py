name = ["a", "b"]
name.append("c")
print(name)

name.insert(1,"d")
print(name)

print(name.pop()) #pop 제일 끝 index 삭제
print(name)

num_list = [5,2,3,1,4]
num_list.extend(name) #두개의 list 합치기
print(num_list)
