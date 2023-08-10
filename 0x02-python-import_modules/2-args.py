#!/usr/bin/python3
if __name__ == "__main__":

    import sys

if (len(sys.argv) - 1) >= 0:
    if (len(sys.argv) - 1) == 1:
        tag = "argument"
    else:
        tag = "arguments"

    if (len(sys.argv) - 1) == 0:
        sign = "."
    else:
        sign = ":"
    print("{} {}{}".format((len(sys.argv) - 1), tag, sign))
