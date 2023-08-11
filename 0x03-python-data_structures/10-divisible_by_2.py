#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_array = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_array.append(True)
        else:
            new_array.append(False)
    return new_array
