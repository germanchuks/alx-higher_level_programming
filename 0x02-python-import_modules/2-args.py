#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        count_str = 'arguments.'
    elif count == 1:
        count_str = 'argument:'
    else:
        count_str = 'arguments:'
    print("{} {}".format(count, count_str))
    for i, item in enumerate(sys.argv):
        if i != 0:
            print("{}: {}".format(i, item))
