def add(a, b):
    a += b
    return a


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == "__main__":
    # a = 1
    # b = 2
    # c = add(a, b)
    # print("a: {a}, b: {b}, c: {c}".format(a=a, b=b, c=c))
    #
    # a = [1, 2]
    # b = [3, 4]
    # c = add(a, b)
    # print("a: {a}, b: {b}, c: {c}".format(a=a, b=b, c=c))
    #
    # a = (1, 2)
    # b = (3, 4)
    # c = add(a, b)
    # print("a: {a}, b: {b}, c: {c}".format(a=a, b=b, c=c))

    company1 = Company("Google", ["a", "b"])
    company1.add("c")
    company1.remove("a")
    print(company1.staffs)

    company2 = Company("Facebook")
    company2.add("d")
    print(company2.staffs)

    company3 = Company("Amazon")
    company3.add("e")
    print(company2.staffs)
    print(company3.staffs)
    print(company2.staffs is company3.staffs)

    print(Company.__init__.__defaults__)
