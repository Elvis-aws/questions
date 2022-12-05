
# Bubble sort
myArray = [8,2,0,4,9,7,4,22,25,19,11,88]


def sortArray():
    # Go through the list once per element
    # x represents the number of elements in the list that are already sorted
    for x in range(len(myArray)):
        # Compare the pairs of elements that are not yet sorted and swap them
        # -1 means we are not going to compare the last element only pairs in the list
        # -1 is very important as we compare two elements thus we cannot compare only the 
        # last element in the array
        for y in range(len(myArray)-x-1):
            # swap if possible
            if myArray[y] > myArray[y + 1]:
                myArray[y], myArray[y + 1] = myArray[y + 1], myArray[y]

    print(f'The sorted list {myArray} is:', myArray)


sortArray()
