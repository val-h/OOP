class Employee:

    # Class variables
    num_of_emp = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emp += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# First Employee
emp_1 = Employee('Valentin', 'Mirchev', 15000)

# Testing out the raise amount
print(Employee.raise_amount)
Employee.raise_amount = 1.13    # Sets the raise_amount for the whole class not just 1 instance

print(f'{emp_1.fullname()} - Day shift pay: {emp_1.pay}')
emp_1.apply_raise()
print(f'{emp_1.fullname()} - Evening shift pay: {emp_1.pay} with raise - {Employee.raise_amount}')

# Second Employee
emp_2 = Employee('Stoyan', 'Peev', 20000)

print(Employee.num_of_emp)
