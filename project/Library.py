class Library(User) :
    def __init__(self, id) :
        self.id = id
        if id in User.member :
            print("hello, "+ id)

        else :
            print("you are not member")
