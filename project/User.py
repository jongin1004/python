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

    def total_user_info(self) :
        for i in User.member["id"] :
            print(i)
