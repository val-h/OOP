class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()
emp_3 = Employee()

print(emp_1)
print(emp_2)
print(emp_3)

emp_1.first = 'Valentin'
emp_1.last = 'Mirchev'
emp_1.email = 'V.Mirchev@bsks.com'
emp_1.pay = 15000

emp_2.first = 'Stoyan'
emp_2.last = 'Peev'
emp_2.email = 'S.Peev@bsks.com'
emp_2.pay = 20000

emp_3.first = 'Ivan'
emp_3.last = 'Peykov'
emp_3.email = 'I.Peykov@bsks.com'
emp_3.pay = 25000

print(emp_2.first)
print(emp_1.last)
print(emp_3.email)

# Thats pretty much it. Going to continue it in another file
