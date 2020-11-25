movie_rank = ['Dr.stange','lucky','movie']
print(movie_rank)
#append() list 맨 뒤에 추가 된다
movie_rank.append('batman')
print(movie_rank)
#insert()를 사용하면 어느 부분에 추가하고 싶은지 인덱스 번호를 정하고 추가하고 싶은 data를 적으면 된다.
movie_rank.insert(1,"superman")
print(movie_rank)

del movie_rank[3]
print(movie_rank)

#del을 사용하면 삭제되고 다시 인덱싱 되므로 여러개를 삭제할 때에는 순서를 잘 생각해서 삭제해야함
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
#list를 더하면 하나의 list로 만들 수 있다.
lang1 = ["c", "c++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

nums =[1,2,3,4,5]
print(sum(nums))

cook = ["pizza","kimbab","ramen"]
print(len(cook))

nums = [1,2,3,4,5]
total = sum(nums)/len(nums)
print(total)
