
# If the number is divisible by 2, then we called it as even. And the remaining ones (not divisible by 2) called 
# as odd numbers.


def get_odd_numbers(list_of_numbers):
    odd_list = []
    for x in list_of_numbers:
        if(x % 2 != 0):
            odd_list.append(x)
    print(odd_list)


print(get_odd_numbers([3,45,6,7,9,0,4,33,2,1,23]))



def get_even_numbers(list_of_numbers):
    odd_list = []
    for x in list_of_numbers:
        if(x % 2 == 0):
            odd_list.append(x)
    print(odd_list)


print(get_even_numbers([3,45,6,7,9,0,4,33,2,1,23]))
