class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __str__(self):
        return ",".join(self.employee)

    def __repr__(self):
        return ",".join(self.employee)


company = Company(["tom", "bob", "jane"])
# if not implement __getitem__
# employee = company.employee

# __getitem__
for e in company:
    print(e)

# __str__
print(company)

# __repr__
company
