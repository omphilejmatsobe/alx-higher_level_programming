#!/usr/bin/python3
for i in range(0, 26, 2):
    print("{}{}".format(chr(122 - i), chr(89 - i)), end="")
