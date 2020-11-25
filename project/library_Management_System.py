class User :
    administrator = ["jong"]
    member = {"name" : [] , "id" : []}

    def __init__(self) :
        pass

    def registration(self, id, name) :
        self.id = id
        self.name = name

        if id not in User.member :
            User.member["name"].append(name)
            User.member["id"].append(id)
            print("successfully registrate")

        else  :
            print("This id is already registrated")

    def user_info(self) :
        self.index = User.member["name"].index(self.name)
        print("name : "+User.member["name"][self.index],
              "id : " + str(User.member["id"][self.index]))


class Library(User) :

    def __init__(self, id) :
        self.id = id
        if id in User.member :
            print("hello, "+ id)

        else :
            print("you are not member")


a = User()
a.registration(2013310045, "jongin")
a.user_info()

b = User()
b.registration(2014310045, "jin")
b.user_info()

c = Library(2013310045)
