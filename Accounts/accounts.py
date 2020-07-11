class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.type = None
        self.bio = None
    
    def Details(self):
        print('Type: ', self.type)
        if self.bio:
            print('Bio: ', self.bio)
    
    def Bio(self):
        print('Write your bio:')
        while True:
            try:
                bio = input('\t- ')
            except ValueError:
                print('Error! Try again.')
            else:
                self.bio = bio
                print('Success! Bio created.')
                break
    
class User(Account):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.type = 'user'

class Admin(Account):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.type = 'admin'
