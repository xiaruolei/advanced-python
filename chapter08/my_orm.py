import numbers

class IntField:
    def __init__(self, min_value=None, max_value=None):
        self._value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("That was no valid number.")
        if value < 0:
            raise ValueError("Number is negative")
        self.value = value

class CharField:
    pass


class User:
    name = CharField(db_column="", max_length=10)
    age = IntField(db_column="", min_value=0, max_length=100)

    class Meta:
        db_table = "user"

if __name__ == "__main__":
    user = User()
    user.name = "Bob"
    user.age = 20
    user.save()
