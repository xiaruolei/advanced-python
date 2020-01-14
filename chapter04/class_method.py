class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and (0 < int(month) <= 12) and (0 < int(day) <= 31):
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == "__main__":
    new_day = Date(2020, 1, 10)
    print(new_day)
    new_day.tomorrow()
    print(new_day)

    # 2020-01-12
    date_str = "2020-01-12"
    year, month, day = tuple(date_str.split("-"))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # staticmethod
    new_day = Date.parse_from_string(date_str)
    print(new_day)
    print(Date.valid_str("2020-01-31"))

    # classmethod
    new_day = Date.from_string(date_str)
    print(new_day)
