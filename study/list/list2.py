price = ['20180728', 100, 130]
print(price[1:])

nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])
print(nums[1::2])
print(nums[::-1])

interest = ['samsung', 'LG', 'KT']
print(interest[::2])
print(interest[0],interest[2])
#join() " "에 특수 문자를 넣으면 각 원소사이에 특수문자가 들어간 채로 하나의 string 구조로 만들어 준다.
interest = ['samsung', 'LG', 'KT', 'daewoo', 'SK']
print(" ".join(interest))
#split() " "에 특수 문자를 기준으로 나눠서 배열형태로 만들어준다.
string = "SAMSUNG/KT/LG"
print(string.split("/"))
#sort() 리스트에 있는 원소를 오름차순으로 정리
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
data2 =  sorted(data)
print(data , data2)
