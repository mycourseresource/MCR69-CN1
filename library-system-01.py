users = {'user':[
    {'userN': 'Adam', 'userP': '11234', 'userH': 'Adamos', 'fails': 0, 'books': {}},
    {'userN': 'Breda', 'userP': '21234', 'userH': 'Ms Virtue', 'fails': 0, 'books': {}},
    {'userN': 'Charlie', 'userP': '31234', 'userH': 'Ms Virtue', 'fails': 3, 'books': {}}
    ]}


def loginProcess():
    print('Login Process Start')
    userName = input('Enter User Name: ')
    print('User Name Entered: ', userName)
    if checkUserName(userName) == True:
        print(checkUserBlocked(userName))
    else:
        loginProcess()    # function recursion - a python function can call itself


def checkUserBlocked(userName):
    # if fails < 3 return false
    # otherwise return true
    for x in users['user']:
        if x['userN'] == userName:
            if x['fails'] < 3:
                return False
    return True


def checkUserName(userName):
    # if username is not found return false
    # if username is found return true
    for x in users['user']:
        print(x)
        if x['userN'] == userName:
            return True
    return False


loginProcess()