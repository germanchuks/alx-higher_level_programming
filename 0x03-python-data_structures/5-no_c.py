#!/usr/bin/python3
def no_c(my_string):
    newString = ''.join([item for item in my_string if item not in 'cC'])
    return newString
