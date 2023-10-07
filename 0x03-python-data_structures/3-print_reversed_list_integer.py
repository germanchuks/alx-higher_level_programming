#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        [print("{:d}".format(my_list[x]))
            for x in range(len(my_list) - 1, -1, -1)]
