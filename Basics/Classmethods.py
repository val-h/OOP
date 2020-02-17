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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
emp_str_1 = 'John-Doe-80000'
emp_str_2 = 'Stoyan-Peev-70000'
emp_1 = Employee('Valentin', 'Mirchev', 15000)

Employee.set_raise_amount(1.15)

print(emp_1.raise_amount)

newEmp = Employee.from_string(emp_str_1)

print(newEmp.email + ' - ' + newEmp.pay)

