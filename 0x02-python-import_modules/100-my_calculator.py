#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    numArg = len(sys.argv) - 1

    if numArg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == ("*" or "-" or "+" or "/"):
        if sys.argv[2] == "*":
            res = cal.mul(a, b)
        elif sys.argv[2] == "+":
            res = cal.add(a, b)
        elif sys.argv[2] == "-":
            res = cal.sub(a, b)
        elif argv[2] == "/":
            res = cal.div(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, res))
    else:
        print("Unkwon operator. Available operator: +, -, * and /")
