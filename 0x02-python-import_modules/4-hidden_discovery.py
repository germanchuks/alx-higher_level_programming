#!/usr/bin/python3

import py_compile

if __name__ == "__main__":
    import hidden_4

    moduleNames = dir(hidden_4)

    filtrdNames = [name for name in moduleNames if not name.startswith("__")]
    filtrdNames.sort()

    for name in filtrdNames:
        print(name)
