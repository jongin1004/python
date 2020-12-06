#집합( set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"a","b","c"}
python = set(["a","d"])

#교집합 (java와 python 둘다 속한 원소)
print(java & python)
print(java.intersection(python)) #intersection & 와 같은 기능

#합집합 (java나 python 둘중에 하나에 속한 원소)
print(java | python)
print(java.union(python))

#차집합(java에는 있지만 python에는 없는 원소)
print(java - python)
print(java.difference(python))

# python에 속한 사람이 늘어남
python.add("b")
print(python)

# java에 속한 사람이 빠짐
java.remove("c")
print(java)
