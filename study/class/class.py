class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self) :
        print("name : "+areum.name+", age : "+str(areum.age)+", gender : "+areum.gender)

    def setInfo(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("end")
# areum = Human()

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

areum = Human("jongin", 27, "nam")
print(areum.name)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("name : "+areum.name+", age : "+str(areum.age)+", gender : "+areum.gender)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
