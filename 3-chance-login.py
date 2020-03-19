# This script just has one flaw, can you guess?


users = {'user': [
    {'userN': 'Adam', 'userP': '11234', 'attempt': 0},
    {'userN': 'Breda', 'userP': '21234', 'attempt': 0},
    {'userN': 'Charlie', 'userP': '31234', 'attempt': 0},
    {'userN': 'Dave', 'userP': '41234', 'attempt': 0}
    ]}


loginGood = False

for x in users['user']:
    if loginGood == False:
        enteredUn = input('Enter your user name: ')
        if x['userN'] == enteredUn:
            print('found the user name')
            for y in range (x['attempt'], 3):
                enteredPw = input('Enter your password: ')
                if x['userP'] == enteredPw:
                    print('correct password')
                    loginGood = True
                    x['attempt'] = 0
                    break
                else:
                    print('incorrect password')
                    loginGood = False
                    x['attempt'] = x['attempt'] + 1
            break

if loginGood == True:
    print('Successful Login')
else:
    print('Unsuccessful Login')
