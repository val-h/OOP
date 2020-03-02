from datetime import datetime as dt

students = {}

class Student:

    def __init__(self, name):
        
        self.name = name
        self.dates = []
        self.comments = []
    
    def AddDate(self, attended_dates):
        # I can just store the dates as they are but i need more practice on them : |
        for date in attended_dates:
            self.dates.append(dt.strptime(date, '%d/%m/%Y'))
    
    def AddComment(self, ment_comment):
        self.comments.append(ment_comment)

    def PrintInfo(self):
        print('\n' + self.name)

        print('\nComments:')
        for comment in self.comments:
            print('\t' + comment)
        else:
            print(f'\tNo comments for {self.name}... :/')

        print('\nDates attended:')
        for date in sorted(self.dates):
            date = dt.strftime(date, '%d/%m/%Y')
            print(f'\t{date}')

# Dates loop
print('\t - Dates - ')
while True:
    cmd = input('/> ')
    if cmd == 'end of dates':
        break
    
    # Splits the name from the dates
    stud_details = cmd.split()
    # Splits all of the dates
    stud_dates = stud_details[1].split(',')

    students[stud_details[0]] = Student(stud_details[0])
    students[stud_details[0]].AddDate(stud_dates)

# Comments loop
print('\t - Comments - ')
while True:
    cmd = input('/> ')
    if cmd == 'end of comments':
        break

    stud_details = cmd.split('-')

    if stud_details[0] in students:
        students[stud_details[0]].AddComment(stud_details[1])

# Output

for stud in students:
    students[stud].PrintInfo()
