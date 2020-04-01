import os

def prtMenu(message):
    os.system('clear')
    print('''
    =========== Library System ===========

             (B) Borrowed Books
             (R) Return Books
             (C) Check Out Books
             (P) Print Loan History
             (W) Change Password

             (Q) Logout

    ''')
    print(message)
    selection = input('Enter your menu option: ')
    selection = selection.strip()
    if selection in ['B', 'b', 'R', 'r', 'C', 'c', 'P', 'p', 'W', 'w', 'Q', 'q']:
        os.system('clear')
        return selection
    else:
        message = 'Invalid Selection. Try Again!'
        prtMenu(message)
