#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dictionary = a_dictionary.copy()
    list_keys = list(copy_dictionary.keys())

    for i in list_keys:
        copy_dictionary[i] *= 2

    return (copy_dictionary)
