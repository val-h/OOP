stud_count = int(input('Number of students: '))
students = []
# Define the student class with the following attributes: name, grade list and average list
class Student:

    def __init__(self, name, grd_list):
        self.name = name
        self.grades = [int(x) for x in grd_list.split()]
        self.avg_grade = sum(self.grades) / len(self.grades)

for i in range(0, stud_count):
    temp_student = input('Student infor: ')
    temp_stud_name = temp_student[0]
    temp_stud_grades = temp_student[1:].split()
    temp_student = Student(temp_student[0], temp_stud_grades)

# Fix this
print(students)

    
