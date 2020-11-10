apart = [ [101, 102], [201, 202], [301, 302] ]

for row in apart:
    for col in row:
        print(col, "room")
        print("-" * 5)

for row in apart:
    for col in row:
        print(col, "room")
    print("-----")


for row in apart:
    for col in row:
        print(col, "room")
print("-" * 5)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)
    result.append(sub)
print(result)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:] :
    print(line[3])

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

for line in ohlc[1:] :
    if line[3] > 150 :
        print(line[3])

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

for line in ohlc[1:] :
    if line[3] >= line[0] :
        print(line[3])

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

volatility = []
for line in ohlc[1:] :
    volatility.append(line[1] - line[2])
print(volatility)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

for line in ohlc[1:] :
    if line[3] > line[0] :
        print(line[1]-line[2])

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

profit = []
for line in ohlc[1:] :
    profit.append((line[3] - line[0]))

print(sum(profit))
