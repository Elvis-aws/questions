import math

# The value of second column is the addition result of first and second column of previous row
# Similarly, the value of third column is the addition result of second and third column of previous row
# and so on

#    1
#   1 1
#  1 2 1
# 1 3 3 1



def pascalsTriangle(n):
    for i in range(n):
        for col in range(n-1, i, -1):
            print(end=" ")
        for col in range(i+1):
            val = int(math.factorial(i)/(math.factorial(col)*math.factorial(i-col)))
            print(val, end=" ")
        print()


pascalsTriangle(9)