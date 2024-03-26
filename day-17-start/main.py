class User:
    def __init__(self, name):
        self.id=0
        self.name=name
        self.following=0
        self.followers=0
        print("Yeni bir nesne olusturuldu..")

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def printUser(self):
        print("==================================")
        print("Name: "+self.name)
        print(f"Following: {self.following}")
        print(f"Followers: {self.followers}")
        print("==================================")
    pass


user_1 = User("Eren")
user_2 = User("Osman")
user_3 = User("Ece")

user_3.follow(user_1)

user_1.printUser()
user_2.printUser()
user_3.printUser()