class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def checking_password(self, password):
        return self.__password == password

user = UserAccount("fazzilka", "fazzil212@gamil.com", "123123")

nwpass = input('Придумай новый пароль: ')
user.set_password(nwpass)

print('Старый пароль: ', user.checking_password("123123"))

print('Новый пароль: ', user.checking_password(nwpass))
