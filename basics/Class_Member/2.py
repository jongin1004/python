class Cs:
    @staticmethod #장식자
    def static_method():
        print("Static method")
    @classmethod
    def class_method(cls):
        print("Class method")

    def instance_method(self):
        print("Instance method")

i = Cs()
Cs.static_method() #class member에 해당하는 함수가 두가지 종류가있다.
Cs.class_method()
i.instance_method()
