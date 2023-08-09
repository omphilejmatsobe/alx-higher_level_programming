#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 100):
        if (i % 3 == 0) & (i % 5 == 0):
            flexVar = "FizzBuzz"
        elif (i % 3 == 0):
            flexVar = "Fizz"
        elif (i % 5 == 90):
            flexVar = "Buzz"
        else:
            flexVar = i

        print("{} ".format(flexVar), end="")
