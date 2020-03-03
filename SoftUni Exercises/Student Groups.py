from datetime import datetime as dt
from math import ceil
prompt = ''
towns = {}
total_groups = 0

class Town:
    """Creating a Town"""
    def __init__(self, name, seats):
        self.students = []
        self.groups = {}

        self.name = name
        self.seats = int(seats)
        print()

    def AddStudent(self, stud):
        self.students.append(stud)
    
    def CreateGroups(self):
        temp_members = self.students.copy()
        groups_count = ceil(len(self.students) / self.seats)
        for grp in range(1, groups_count + 1):
            self.groups[grp] = Group(self.name, grp)
            for i in range(0, self.seats):
                if len(temp_members) == 0:
                    break
                self.groups[grp].AddMember(temp_members.pop(0))
        return groups_count
    
    def PrintGroups(self):
        print(f'\nGroups in {self.name}:')
        for grp_num in self.groups.keys():
            self.groups[grp_num].PrintInfo()

class Group:

    def __init__(self, town, number):
        """Creating a Group"""
        self.members = []

        self.town = town
        self.num = number
    
    def AddMember(self, member):
        self.members.append(member)
    
    def PrintInfo(self):
        em_list = []
        for member in self.members:
            em_list.append(member.email)
        print(f'\tGroup {self.num} => {", ".join(em_list)}')
    
class Student:
    """Creating a Student"""
    def __init__(self, name, email, date):

        self.name = name
        self.email = email
        self.date = dt.strptime(date, '%d-%b-%Y')

def Help():
    print('\n\t- Help page -\n')
    print('To add a town enter a command in the following format:\n')
    print('T => X')
    print('\tT - name of the town')
    print('\tX - maximum seats per group in that town\n')

    print('To add a Student in that town enter the following command:\n')
    print('name | email | date')
    print('date format: day-month-year')
    print('example -> 15-Jul-1955')

print("\t- Students Groups program -")
print()

city_name = ''
grp_seats = ''
while True:
    cmd = input('')
    if cmd == 'End':
        for town in towns:
            total_groups += towns[town].CreateGroups()
        break

    if '=>' in cmd:
        cmd = cmd.split()
        city_name = cmd[0]
        grp_seats = cmd[2]
        
        towns[city_name] = Town(city_name, grp_seats)
    
    elif '|' in cmd:
        cmd = cmd.split('|')
        std_name = cmd[0].rstrip()
        std_email = cmd[1].strip()
        std_date = cmd[2].lstrip()
        
        towns[city_name].AddStudent(Student(std_name, std_email, std_date))

    elif cmd == 'help':
        Help()
    else:
        print('\nError!\nType help to seea quick start guide.')

# Output

print(f'\nCreated {total_groups} groups in {len(towns)} towns:')

for town in sorted(towns.keys()):
    towns[town].PrintGroups()
