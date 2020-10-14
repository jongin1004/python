movie_rank = ("Dr.strange", "lucky", "movie")

#하나의 원소만 들어갈 경우에는 tuple이 되지않느다 그래서 뒤에 ","를 붙혀줘야 한다.
my_tuple = (1,)
print(type(my_tuple))
#tuple은 원칙적으로 ()로 정의 되어야 하지만, 생략되어도 동작
t = 1,2,3,4
print(type(t))
#tuple은 원소를 재정의하는 것이 불가능하다. 따라서 다시 새로운 변수에 만들어줘야 한다.
#t[0] = "A" LIST 처럼 이렇게 재정의 해주는 것이 불가능하다.
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)
# list() tuple을 list로 변경
interest = ("samsung", "LG", "KT")
print(type(list(interest)))
#데이터 언팩킹
temp = ('apple', 'banana' , 'cake')
a, b, c = temp
print(a, b, c)
#tuple(range()) min , max , 간격 으로 tuple생성
data = tuple(range(2,100,2))
print(data)
