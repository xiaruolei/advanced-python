class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "x: {x}. y: {y}".format(x=self.x, y=self.y)


first_vec = Vector(1, 2)
second_vec = Vector(2, 3)
print(first_vec + second_vec)