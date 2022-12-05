
myString = 'Ngwesse'

def remoDuplicate():
    resultString = ''
    for x in myString:
        if x not in resultString:
            resultString = resultString + x
    print(f'New string from {myString} is:', resultString)

remoDuplicate()