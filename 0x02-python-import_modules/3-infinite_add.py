#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum = 0;

    for x in range(1, len(sys.argv)):
            sum += sys.argv[x]
    print(sum)
