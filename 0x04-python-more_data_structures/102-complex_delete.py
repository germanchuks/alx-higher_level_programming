#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    target_keys = [key for key, target_value in a_dictionary.items()
                   if target_value == value]
    for key in target_keys:
        del a_dictionary[key]
    return a_dictionary
