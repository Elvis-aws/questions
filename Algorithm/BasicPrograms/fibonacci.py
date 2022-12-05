
# Fibonacci series are formed in a way that, the first two terms are 0 and 1, rest of all the terms are in a 
# way that, the next term is the summation of previous two terms. For example, the first 8 terms of Fibonacci 
# series are: 0, 1, 1, 2, 3, 5, 8, 13.

def printFibonacci(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
        # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
        # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
       
printFibonacci(20)



    
    