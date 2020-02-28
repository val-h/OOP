stud_count = int(input('Number of students: '))
students = []
good_students = []
# Define the student class with the following attributes: name, grade list and average list
class Student:

    def __init__(self, name, grd_list):
        self.name = name
        self.grades = grd_list
        self.avg_grade = sum(self.grades) / len(self.grades)

for i in range(0, stud_count):
    temp_student = input('Student info: ')
    temp_student = temp_student.split()
    temp_stud_name = temp_student.pop(0)
    temp_stud_grades = [float(x) for x in temp_student]
    students.append(Student(temp_stud_name, temp_stud_grades))

for stud in students:
    if stud.avg_grade >= 5:
        good_students.append(stud)

for stud in sorted(good_students, key=lambda x: x.name):    # Learn more about lambda and sorting class instances in lists
    print(f'{stud.name} -> {stud.avg_grade:.2f}')
