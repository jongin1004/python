class Facebook :
    def __init__(self, name, id) :
        self.name = name
        self.id = id
        self.follower = []

    def get_id(self) :
        return self.id

    def get_name(self) :
        return self.name

    def add_follow(self, id) :
        self.follower.append(id)

    def get_follower(self) :
        return self.follower

u_1 = Facebook("jong", "bill1224")
u_2 = Facebook("kim", "kim2014")
u_3 = Facebook("ha", "ha2013")

print(u_1.get_id())
print(u_1.get_name())
u_1.add_follow("kim")

print(u_1.get_follower())
