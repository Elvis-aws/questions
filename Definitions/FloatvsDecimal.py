
# Both the float and decimal types store numerical values in Python
# Generally, decimals exist in Python to solve the precision issues of floats.

# Floats
# Use floats when convenience and speed matter. A float gives you an approximation of the number you declare. 
# For example, if I print 0.1 with 18 decimals places, I don’t actually get 0.1 but instead an approximation.

print(f"{0.1:.18f}")
0.100000000000000006

# Similarly, when doing operations, such as addition with floats, you get an approximation, which can lead 
# confusing code, such as the following.

.1 + .1 + .1 == .3
False
.1 + .1 + .1
0.30000000000000004


# Decimals
# Use decimals when precision matters, such as with financial calculations. Decimals can suffer from their own 
# precision issues, but generally, decimals are more precise than floats. The performance difference between 
# float and decimal, with Python 3, is not outlandish, and in my experience, the precision benefits of a decimal 
# outweigh the performance benefits of a float.


from decimal import Decimal
print(f"{Decimal('0.1'):.18f}")
0.100000000000000000
Decimal('.1') + Decimal('.1') + Decimal('.1') == Decimal('.3')
True


