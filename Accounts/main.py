import json

from accounts import User, Admin

accounts = []

logged_usr = None

def Register():
    print('Register an account.')
    while True:
        try:
            username = input('Username: ')
            password = input('Password: ')
            rep_pass = input('RePass: ')
            acc_type = input('Account type(user/admin): ')
        except ValueError:
            print('Error! Invalid input.')
        else:
            if acc_type == 'user':
                _RegUser(username, password)
            elif acc_type == 'admin':
                _RegAdmin(username, password)
            break

def _RegUser(username, password):
    accounts.append(User(username, password))

def _RegAdmin(username, password):
    accounts.append(Admin(username, password))

def Login():
    attempts = 3
    while attempts != 0:
        try:
            username = input('Username: ')
            for acc in accounts:
                if acc.username == username:
                    password = input('Password: ')
                    if acc.password == password:
                        print(f'Logged in {acc}', type(acc))
                        return acc
            else:
                attempts -= 1
                print('Wrong credentials', attempts)
        except ValueError:
            attempts -= 1
            print('Wrong credentials.', attempts)
    return None

def Logout():
    print('Logging out of', logged_usr)

while True:
    usr_inp = input('/> ')
    if usr_inp == 'q':
        print('Quiting...')
        quit()
    
    elif usr_inp == 'register':
        Register()
    elif usr_inp == 'login':
        logged_usr = Login()
    elif usr_inp == 'logout':
        logged_usr = None
    # Test command
    elif usr_inp == 'accs':
        print('Accounts len -', len(accounts))
        for acc in accounts:
            print(acc, type(acc))

    elif logged_usr:
        if usr_inp == 'details':
            logged_usr.Details()
        elif usr_inp == 'bio':
            logged_usr.Bio()
        else:
            print('Error.')

    else:
        print('Wrong Input.')
