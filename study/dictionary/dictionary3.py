cabinet = {3:"a", 100:"b", 12:"c"}

# print(cabinet[5]) #dic의 키값으로 value를 불러오는데
                    #존재하지 않는 키값이면 오류가 뜸

print(cabinet.get(5)) #get을 사용하면 존재하지 않는 키값일 땐
                      #none을 출력해줌

print(cabinet.get(5,"empty")) #none대신 원하는 메세지 정할 수 있음

print(3 in cabinet) # key in dic 하면 key값이 dic 안에 존재하는지
                    # 유무를 true , false 로 출력

del cabinet[3] #key 삭제
print(cabinet)

cabinet.clear()
print(cabinet)
