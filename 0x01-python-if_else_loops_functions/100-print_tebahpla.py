#!/usr/bin/python3
def printReverseASCII():
    for i in reversed(range(97, 123)):
        letter = chr(i)
        if i % 2 != 0:
            letter = chr(i - 32)
        print("{}".format(letter), end='')


printReverseASCII()
