


def bubbleSort( theSeq ):
    n = len( theSeq ) #  Gets the length of the array and assigns the value to a variable n

    for i in range( n - 1 ) : # Starts a for loop that runs the bubble sort algorithm (n – 1) times. 
                              # -1 implies it will not sort the last single element in the loop since it compares during sorting
                              # This is the outer loop.
        flag = 0  #  Defines a flag variable that will be used to determine if a swap has occurred or not.
                  # This is for optimization purposes

        for j in range(n - 1) : #  Starts the inner loop that compares all the values in the list from the 
                                # first to the last one.
            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1

        if flag == 0: # Uses an if statement to check if the value of the variable flag is 0
            break

    return theSeq

el = [21,6,9,33,3] 

result = bubbleSort(el)

print (result)


