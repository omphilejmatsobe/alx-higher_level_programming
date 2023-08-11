#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    numArg = len(sys.argv) - 1

    if numArg < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit (1)

