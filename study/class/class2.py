class Stock:
    def __init__(self, name, code, per, pbr, earing):
        self.name = name
        self.code = code
        self.per = float(per)
        self.pbr = float(pbr)
        self.earing = float(earing)

    def set_name(self, name) :
        self.name = name

    def set_code(self, code) :
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per) :
        self.per = per

    def set_pbr(self, pbr) :
        self.pbr = pbr

    def set_earing(self, earing) :
        self.earing = earing

#
# samsung = Stock("Samsung", "005930")
# print(samsung.name)
# print(samsung.code)
#
#
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#
# a = Stock(None, None)
# a.set_name("Samsung")
# a.set_code("005930")
# print(a.name)
# print(a.code)
#
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#
# print(samsung.get_name())
# print(samsung.get_code())

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")

sam = Stock("Samsung", "005930", 15.79, 1.33, 2.83)
print(sam.name)
print(sam.code)
print(sam.per)
print(sam.pbr)
print(sam.earing)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")

a = Stock("Samsung", "005930", 15.79, 1.33, 2.83)
print(a.set_per(12.75))

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")

list = []

samsung = Stock("samsung", "005930", 15.79, 1.33, 2.83)
hyundae = Stock("hyundae", "005380", 8.70, 0.35, 4.27)
LG = Stock("LG", "066570", 317.34, 0.69, 1.37)

list.append(samsung)
list.append(hyundae)
list.append(LG)

for i in list:
    print(i.code, i.per)
