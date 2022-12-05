

def get_negative_numbers(list_of_numbers):
    negative_list = []
    for x in list_of_numbers:
        if(x < 0):
            negative_list.append(x)
    print(negative_list)

print(get_negative_numbers([-1,2,6,55,-22,-55,0]))