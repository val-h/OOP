"""OOP, explained by NeuralNine, Just going through his intermediate tuttorials."""

class Person:
    """A class to represent a person and a few basic attributes."""

    age_multiplier = 1
    people = []

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.people.append(self)

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Height: {self.height}cm'

    def get_older(self):
        self.age += Person.age_multiplier

class Worker(Person):
    """A DECORA worker. Still."""

    def __init__(self, name, age, height, salary):
        super().__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super().__str__()
        text += f', Salary: {self.salary}'
        return text

    def yearly_salary(self):
        return self.salary * 12
