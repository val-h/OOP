import datetime
class Employee:

    num_of_emp = 0
    raise_amount = 1.13

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emp += 1

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
emp_1 = Employee('Valentin', 'Mirchev', 15000)

my_date = datetime.date(1997, 8, 24)

print(Employee.is_workday(my_date))
