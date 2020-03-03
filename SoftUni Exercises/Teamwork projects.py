teams_count = int(input('Number of teams: '))

prompt = '/> '  # Just trying this - i haven't used it before
teams = {}
total_members = []

class Team:

    def __init__(self, name, leader):
        
        self.members = []

        self.name = name
        self.leader = leader
        total_members.append(leader)

        print(f'Team {name} has been created by {leader}!')
    
    def Join(self, name):
        self.members.append(name)
        total_members.append(name)
    
    def PrintMembers(self):
        print(f'\n{self.name}:')
        print(f'Leader - {self.leader}')
        for member in sorted(self.members):
            print(f'\t-- {member}')

while True:
    cmd = input(prompt)
    if cmd == 'end of assignment':
        break
    
    member_info = ''
    if '->' in cmd:
        member_info = cmd.split('->')
        if member_info[1] not in teams:
            print(f'Team {member_info[1]} doesn\'t exist!')
        elif member_info[0] in total_members:
            print(f'Member {member_info[0]} cannot join team {member_info[1]}')
        else:
            teams[member_info[1]].Join(member_info[0]) 

    elif '-' in cmd:
        member_info = cmd.split('-')
        if member_info[1] in teams:
            print(f'Team {member_info[1]} was already created!')
        elif member_info[0] not in teams.values():
            teams[member_info[1]] = Team(member_info[1], member_info[0])
        else:
            print(f'{member_info[0]} can\'t create another team!')
    else:
        print('Error in spliting the mmeber information!')

# Output
to_disband = []
for team in sorted(teams.keys()):
    if len(teams[team].members) == 0:
        to_disband.append(team)
    else:
        teams[team].PrintMembers()

print('\nTeams to disband:')
for team in to_disband:
    print(f'\t{team}')
