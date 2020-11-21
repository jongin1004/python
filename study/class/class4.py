class Car :
    def __init__(self, tire, price) :
        self.tire = tire
        self.price = price

class Bicycle(Car) :
    def __init__(self, tire, price, drive):
        super().__init__(tire, price)
        #Car.__init__(self, tire, price)
        self.drive = drive

class Vehicle(Car) :
    def info(self) :
        print(self.tire)
        print(self.price)


car = Car(2, 1000)
# print(car.tire)
# print(car.price)

bicycle = Bicycle(2, 100, "simano")
print(bicycle.price)
print(bicycle.drive)


car_info = Vehicle(3, 1000)
car_info.info()


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

class Class1:
    def __init__(self):
        print("1")

    def call(self):
        print("1")

class Class2(Class1):
    def __init__(self):
        print("2")
        super().__init__()

    def call(self):
        print("2")


my = Class2()
print("@@@@@@@@@@@@@@@@@@@@@@")
my.call()
