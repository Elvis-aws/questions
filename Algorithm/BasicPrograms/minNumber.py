

def printMinNumber():
    series = [67,33,43,23,43,23,43,999]
    minNumber = series[0]

    for numbers in series:
        if numbers < minNumber:
            minNumber = numbers
    print(minNumber)

printMinNumber()