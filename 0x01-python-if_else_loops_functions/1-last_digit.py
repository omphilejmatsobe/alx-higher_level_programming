#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = ""

if number < 0:
    last = 10 - (number % 10)
    last = last * (-1)
elif number >= 0:
    last = number % 10

if last > 5:
    string = "and is greater than 5"
elif last == 0:
    string = "and is 0"
elif last < 6:
    string = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, last, string))
