class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a dog")


class Duck(object):
    def say(self):
        print("i am a duck")


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __str__(self):
        return ",".join(self.employee)


# all implement say()
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

# Extend list by appending elements from the iterable
a = ["a1", "a2"]
b = ["b1", "b2"]
s = set()
s.add("s1")
s.add("s2")

# extend a list
a.extend(b)
print(a)
# extend a set
a.extend(s)
print(a)
# extend a iterable object
company = Company(["Google", "Facebook"])
a.extend(company)
print(a)
