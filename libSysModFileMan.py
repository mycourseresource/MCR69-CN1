import io, json

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
    else:
        return {'user':[
    {'userN': 'Adam', 'userP': '11234', 'userH': 'Adamos', 'fails': 0, 'books': {
        'borrow': [
            {'id': 0, 'dateOut': '', 'dateRtn': ''}
        ],
        'order': [
            {'id': 0, 'dateOut': '', 'dateRtn': ''}
        ],
        'history': [
            {'id': 0, 'dateOut': '', 'dateRtn': ''}
        ]
    }},
    {'userN': 'Breda', 'userP': '21234', 'userH': 'Ms Virtue', 'fails': 1, 'books': {}},
    {'userN': 'Charlie', 'userP': '31234', 'userH': 'Ms Virtue', 'fails': 2, 'books': {}},
    {'userN': 'David', 'userP': '41234', 'userH': 'Ms Virtue', 'fails': 3, 'books': {}}
    ]}

