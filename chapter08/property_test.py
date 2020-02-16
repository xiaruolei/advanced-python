from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self._age = 0
        self._name = name
        self.birthday = birthday

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def name(self):
        return self._name + "."

    @name.setter
    def name(self, value):
        self._name = value


print("current path: {}".format(__file__))

if __name__ == "__main__":
    user = User("Tom", date(year=2000, month=2, day=11))
    print(user.get_age())

    print(user._name)
    print(user.name)

    user.name = "Jim"
    print(user._name)
    print(user.name)