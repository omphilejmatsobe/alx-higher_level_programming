#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    length = len(sys.argv) - 1
    if length == 1:
        string = "argument:"
    elif length == 0:
        string = "arguments."
    else:
        string = "arguments:"

    print("{} {}".format(length, string))

    for i in range(length):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
