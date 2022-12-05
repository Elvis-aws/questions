

def printMaxNumber():
    series = [67,33,43,23,43,23,43,999]
    largestNumber = series[0]

    for numbers in series:
        if numbers > largestNumber:
            largestNumber = numbers
    print(largestNumber)

printMaxNumber()
        
