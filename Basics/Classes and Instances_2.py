class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def FullName(self):
        return f'{self.first} {self.last} '


emp_1 = Employee('Valentin', 'Mirchev', 15000)
emp_2 = Employee('Stoyan', 'Peev', 20000)
emp_3 = Employee('Ivan', 'Peykov', 25000)

print(Employee.FullName(emp_2))
print(emp_1.FullName())
print(emp_3.email)
print(Employee.FullName(emp_1) + emp_1.email)

