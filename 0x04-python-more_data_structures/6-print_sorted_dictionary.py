#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    [print("{}: {}".format(key, value)) for key, value in sorted_dict.items()]
    return sorted_dict
