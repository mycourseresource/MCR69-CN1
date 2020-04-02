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
    {'userN': 'Adam', 'userP': '11234', 'userH': 'Adamos', 'fails': 0, 'books': {'borrow': [], 'order': [], 'history': []}},
    {'userN': 'Breda', 'userP': '21234', 'userH': 'Ms Virtue', 'fails': 1, 'books': {'borrow': [],'order': [],'history': []}},
    {'userN': 'Charlie', 'userP': '31234', 'userH': 'Ms Virtue', 'fails': 2, 'books': {'borrow': [],'order': [],'history': []}},
    {'userN': 'David', 'userP': '41234', 'userH': 'Ms Virtue', 'fails': 3, 'books': {'borrow': [],'order': [],'history': []}}
    ]}


def readBooks(doIt):
    if doIt == True:
        with open('libBooks.json') as f:
            return json.load(f)
    else:
        return {'inventory':[
    {'id':0, 'Title': 'Python in easy steps', 'Author': 'Mike McGrath', 'ISBN': '9781840788129', 'Format': 'PB', 'onHand': 4, 'borrowed': [],'ordered': []},
    {'id':1, 'Title': 'I\'m an HTML web page builder', 'Author': 'Max Wainewright', 'ISBN': '9781526301048', 'Format': 'HB', 'onHand': 2, 'borrowed': [],'ordered': []},
    {'id':2, 'Title': 'I\'m an HTML web page builder', 'Author': 'Max Wainewright', 'ISBN': '1526301040', 'Format': 'PB', 'onHand': 4, 'borrowed': [],'ordered': []},
    {'id':3, 'Title': 'An Introduction to Python', 'Author': 'Guido Van Rossum', 'ISBN': '978-1906966133', 'Format': 'PB', 'onHand': 1, 'borrowed': [],'ordered': []},
    {'id':4, 'Title': 'Python 3.6 Tutorial', 'Author': 'Guido Van Rossum', 'ISBN': '978-9888406906', 'Format': 'PB', 'onHand': 2, 'borrowed': [],'ordered': []},
    {'id':5, 'Title': 'Pro JavaScript Techniques', 'Author': 'John Resig', 'ISBN': '978-1590597279', 'Format': 'PB', 'onHand': 3, 'borrowed': [],'ordered': []},
    {'id':6, 'Title': 'Just for Fun: The Story of an Accidental Revolutionary', 'Author': 'Linus Torvalds, David Diamond', 'ISBN': '978-0066620732', 'Format': 'PB', 'onHand': 1, 'borrowed': [],'ordered': []},
    {'id':7, 'Title': 'Cognitive Computing: A Brief Guide for Game Changers', 'Author': 'Vint Cerf', 'ISBN': '978-0929652511', 'Format': 'PB', 'onHand': 1, 'borrowed': [],'ordered': []}
    ]}
