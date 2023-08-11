#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    numArg = len(sys.argv) - 1

    if numArg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    sn = 0

    if sys.argv[2] == "*":
        res = mul(a, b)
        sn = 1
    elif sys.argv[2] == "+":
        res = add(a, b)
        sn = 1
    elif sys.argv[2] == "-":
        res = sub(a, b)
        sn = 1
    elif argv[2] == "/":
        res = div(a, b)
        sn = 1
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, res))
