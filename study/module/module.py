import datetime

now = datetime.datetime.now()
print(now)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def time_now() :
    return datetime.datetime.now()

print(time_now())

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

now = datetime.datetime.now()
print(now, type(now))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

import datetime

now = datetime.datetime.now()
print(now.strftime("%Y,%m,%d %H:%M:%S"))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#
# import time
#
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

import os
ret = os.getcwd()
print(ret, type(ret))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

os.rename("D:/python/before.txt", "D:/python/after.txt")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)
