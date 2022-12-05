# Extended Slicing
myString = "Greecks.com"

def reverseStringUsingSlice():
    print(myString[-1::-1])


# reverseStringUsingSlice()

# Using foor loop

def reverseStringUsingForLoop():
    resultSting = ''
    for x in myString:
        resultSting = x + resultSting
    print(f'The reverse string {myString} is:', resultSting)

reverseStringUsingForLoop()