#75번
input_line = input()
#초기 자금과 버스를 몇 번 이용할 것인지에 대한 입력값을 split()을 이용해 함수형태로 받는다.
info = input_line.split(" ")
count = int(info[1])
#버스의 요금에 대한 입력값을 받기위해서 입력 횟수에 비례한 list를 초기화해준다.
price = [0 for _ in range(count)]
for i in range(0,count) :
    price[i] = input()
#초기자금과 포인트 초기화
money = int(info[0])
point = 0
for j in range(0,int(info[1])) :
    if point < int(price[j]) :
        money -= int(price[j])
        point += int(price[j])*0.1
        print(money, round(point))
    else:
        point -= int(price[j])
        print(money, round(point))
