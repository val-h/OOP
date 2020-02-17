class Employee:

    raise_amount = 1.13

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amount = 1.25

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print(f'Employee {emp} is already in the list.')
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('/> ', emp.fullname())

dev_1 = Developer('Valentin', 'Mirchev', 15000, 'Python')
dev_2 = Developer('Stoyan', 'Peev', 20000, 'R')
mgr_1 = Manager('Ivan', 'Peykov', 30000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emp()

print(isinstance(dev_1, Employee))
print(isinstance(mgr_1, Manager))

print(issubclass(Developer, Manager))
print(issubclass(Developer, Employee))
