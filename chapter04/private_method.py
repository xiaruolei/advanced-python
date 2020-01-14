from chapter04.class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2020 - self.__birthday.year


class Student(User):
    def __init__(self, birthday):
        self.__birthday = birthday


if __name__ == "__main__":
    user = User(Date(1993, 1, 1))
    print(user.get_age())
    # _classname__attr
    print(user._User__birthday)

    student = Student(Date(1994, 1, 1))
    print(student._Student__birthday)
