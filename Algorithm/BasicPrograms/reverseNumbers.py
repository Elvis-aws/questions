

def number_in_reverse_order(enteredNumber):
    reverse_list = []
    while(enteredNumber >= 1):
        reverse_list.append(enteredNumber)
        enteredNumber = enteredNumber - 1

    print(reverse_list)

print(number_in_reverse_order(20))