
userNameF = ['Adam', 'Charlie']
balance = [100, 100]

activeUser = 0
#percentage = 2.5



def inputPercentage():
    percentage = input('\nPlease enter the applicable interest rate:')

    try:
        percentage = float(percentage)
        return percentage
    except:
        print ('Please enter numeric values only')
        inputPercentage()

percentage = inputPercentage()



print ('User: ', userNameF[activeUser])

print ('balance pre percentage calculation: ', balance[activeUser])

balance[activeUser] = balance[activeUser] + float(balance[activeUser]) / 100 * percentage

print ('balance post percentage calculation: ', balance[activeUser])
