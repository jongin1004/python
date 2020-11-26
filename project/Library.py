import User

class Library(User.User) :
    def __init__(self, id) :
        self.id = id
        if self.id in User.User.member["id"] :
            self.index = User.User.member["id"].index(self.id)
            print("hello, "+ User.User.member["name"][self.index])

        else :
            print("you are not member")
