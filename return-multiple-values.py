


def returnValuesExample1():
    input('About to return values from returnValuesExample1')
    value1 = 'A String Value'
    value2 = 2020
    value3 = True
    return [value1, value2, value3]

returnValue = returnValuesExample1()
print(returnValue)
print(returnValue[0])
print(returnValue[1])
print(returnValue[2])




def returnValuesExample2():
    input('About to return values from returnValuesExample2')
    value1 = 'Another String Value'
    value2 = 2022
    value3 = False
    return {"value1": value1, "value2": value2, "value3": value3}

returnValue = returnValuesExample2()
print(returnValue)
print(returnValue["value1"])
print(returnValue["value2"])
print(returnValue["value3"])




myDictionary = {"value1": 'A String in a Dictionary', "value2": 2023, "value3": True}
def returnValuesExample3(x):
    input('About to return values from returnValuesExample3')
    x["value1"] = 'A new string modified in returnValuesExample3()'
    x["value2"] = 43
    x["value3"] = False
    return x

returnValue = returnValuesExample3(myDictionary)
print(returnValue)
print(returnValue["value1"])
print(returnValue["value2"])
print(returnValue["value3"])




# # # # # more complex example

def getUsersDict():
    return {"user": [{"userN": 'Adam', "userP": "1234"}, {"userN": 'Breda', "userP": "2345"}]}

def login(users):
    enteredN = input('Enter User Name: ')
    enteredP = input('Enter User Password: ')
    uNValid = checkUserN(users, enteredN)
    # print('uNValid: ', uNValid)
    uPValid = checkUserP(users, uNValid[1], enteredP)
    # print('uPValid: ', uPValid)
    if (uNValid[0] == True and uPValid == True):
        return [enteredN, uNValid[1]]
    else:
        return False


def checkUserN(users, enteredN):
    for i in range(len(users["user"])):
        if users["user"][i]["userN"] == enteredN:
            return [True, i]
    return [False, -1]


def checkUserP(users, index, enteredP):
    # print('users ... userP: ', users["user"][index]["userP"])
    # print('index: ', index)
    # print('int(enteredP): ', int(enteredP))
    if users["user"][index]["userP"] == enteredP:
        return True
    else:
        return False


print(login(getUsersDict()))



