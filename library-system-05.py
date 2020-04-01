import os
# os.system('cls')      # Windows Platform
os.system('clear')    # Linux Platform
import getpass       # this will hide the characters when entering the password


import libSysModFileMan as fileAcc
import libSysModMenu as menu


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
                # password = input('Enter Password:' )
                password = getpass.getpass(prompt='Enter Password:')
                if x['userP'] == password:
                    x['fails'] = 0 # entering the correct password will reset 'fails' to 0
                    fileAcc.saveData(users)
                    return True
                else:
                    print('Incorrect password')
                    x['fails'] = n + 1 # entering the incorrect password will increment 'fails'
                    fileAcc.saveData(users)
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



def displayMenu():
    menuOption = menu.prtMenu('')
    # os.system('clear')
    print('Return value from menuOption: ', menuOption)
    if menuOption == 'B' or menuOption == 'b':
        input('(B) Borrowed Books function not yet available')
        displayMenu()
    elif menuOption == 'R' or menuOption == 'r':
        input('(R) Return Books function not yet available')
        displayMenu()
    elif menuOption == 'C' or menuOption == 'c':
        checkoutBooks()
    elif menuOption == 'P' or menuOption == 'p':
        input('(P) Print Loan History function not yet available')
        displayMenu()
    elif menuOption == 'W' or menuOption == 'w':
        input('(W) Change Password function not yet available')
        displayMenu()
    elif menuOption == 'Q' or menuOption == 'q':
        logoutProcess()


def logoutProcess():
    os._exit(os.EX_OK)
    #   sys.exit    # requires import sys



def checkoutBooks():
    search = input('Enter a full name or fractional name of a book: ')
    search = search.strip()
    # print(books['inventory'][0]['Title'])
    for x in books['inventory']:
        if search.lower() in x['Title'].lower():
            print(x['id'], x['Title'])
    selection = input('Make your selection, or press ENTER to return to Main Menu')
    if selection == '':
        displayMenu()
    # this needs more code .....
    checkoutBooks()


# saveData(users)
users = fileAcc.readData(False)
# print(users)
books = fileAcc.readBooks(False)
# print(books)

print('Return value from loginProcess: ', loginProcess())

displayMenu()

