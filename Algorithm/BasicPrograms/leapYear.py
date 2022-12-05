
# The normal one contains 365 days, but the leap year contains 366 days. Logically, All the years that are perfectly 
# divisible by four called Leap except the century.
# If the century is divisible by 400, then that is a Leap year in Python

def is_leap_year(ya):
    if (ya%400 == 0):
        print("%d is a Leap year" %ya)
    elif (ya%100 == 0):
        print("%d is Not a Leap year" %ya)
    elif (ya%4 == 0):
        print("%d is a Leap year" %ya)
    else:
        print("%d is Not a Leap year" %ya)

print(is_leap_year(2033))