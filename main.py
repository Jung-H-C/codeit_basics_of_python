class User:
    def say_hello(some_user):
        print("안녕하세요! 저는 {}입니다!".format(some_user.name))

    def login(self, my_email, my_password):
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공")
        else:
            print("로그인 실패")

    def check_name(self, name):
        return self.name == name

user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user1.login("captain@codeit.kr", "12345")

print(user1.check_name("김대한"))

print(user1.check_name("김대위"))