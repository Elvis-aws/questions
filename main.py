


numbers = [2,4,1,909,33,21,66,43,3,89,57,8,910]
ent_number = 30
name = 'Elvis'


def my_list(var_entered):
    new_list = []
    for x in var_entered:
        new_list.insert(0,x)
    return new_list

if __name__ == '__main__':
    res = my_list(name)
    print(res)
                
