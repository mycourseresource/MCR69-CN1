import os
# os.system('cls')      # Windows Platform
os.system('clear')    # Linux Platform
import io, json


users = {'user':[
    {'userN': 'Adam', 'userP': '11234', 'userH': 'Adamos', 'fails': 0, 'books': {}},
    {'userN': 'Breda', 'userP': '21234', 'userH': 'Ms Virtue', 'fails': 0, 'books': {}},
    {'userN': 'Charlie', 'userP': '31234', 'userH': 'Ms Virtue', 'fails': 3, 'books': {}},
    {'userN': 'David', 'userP': '41234', 'userH': 'Ms Virtue', 'fails': 2, 'books': {}}
    ]}



def saveData(users):
    # print('users', users)
    strUsers = json.dumps(users, ensure_ascii=False)
    # print('strUsers', strUsers)
    with io.open('libUsers.json', 'w', encoding='utf-8') as f:
        f.write(strUsers)


def readData(doIt):
    if doIt == True:
        with open('libUsers.json') as f:
            # users = json.load(f)
            return json.load(f)




def loginProcess():
    print('Login Process Start')
    userName = input('Enter User Name: ')
    print('User Name Entered: ', userName)
    if checkUserName(userName) == True:
        if checkUserBlocked(userName) == True:
            os.system('clear')
            print('Sorry dear user, but you have been blocked due to 3 false login attempts.')
            return False
        else:
            # print('checkPassword returned: ', checkPassword(userName))
            if checkPassword(userName) == True:
                for x in users['user']:
                    if x['userN'] == userName:
                        #return 'All Good to this line' #{userName, x['userH'], x['books']}
                        return {'userN': userName, 'userH': x['userH'], 'books': x['books']}
            return False # this is he line that had the indentation error during the demo
    else:
        tryAgain = input('Entered user name not valid. Do you want to try again [y/n]')
        if tryAgain == 'y':
            loginProcess()    # function recursion - a python function can call itself
        else:
            return False



def checkPassword(userName):
    for x in users['user']:
        if x['userN'] == userName:
            print('Found User')
            print('This is the first print of fails: ', x['fails'])
            y = range(x['fails'],3)
            for n in y:
                print('This is the second print of fails: ', n)
                password = input('Enter Password:' )
                if x['userP'] == password:
                    x['fails'] = 0 # entering the correct password will reset 'fails' to 0
                    saveData(users)
                    return True
                else:
                    print('Incorrect password')
                    x['fails'] = n + 1 # entering the incorrect password will increment 'fails'
                    saveData(users)
    return False





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
        # print(x)
        if x['userN'] == userName:
            return True
    return False



# saveData(users)
users = readData(True)
print('Return value from loginProcess: ', loginProcess())