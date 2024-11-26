#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(f"{a} + {b} = {add(a, b)}");
    print(f"{a} - {b} = {sub(a, b)}");
    print(f"{a} * {b} = {mul(a, b)}");
    print(f"{a} / {b} = {div(a, b)}");
