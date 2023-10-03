#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        newString = str[:n] + str[n + 1:]
    else:
        newString = str
    return newString
