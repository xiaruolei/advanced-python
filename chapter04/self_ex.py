from chapter04.class_method import Date


class Person:
    """
    Person doc
    """
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == "__main__":
    student = Student("USC")
    # # 通过__dict__查询属性
    # student.__dict__["address"] = "LA"
    # print(student.address)
    # print(student.__dict__)
    # print(Student.__dict__)
    # print(Person.__dict__)
    # print(student.name)

    # # 通过dir查询属性
    print(dir(student))
    a = [1, 2]
    print(dir(a))
