#!/usr/python3
import calculator_1 as cal

a = 10
b = 5

num = cal.add(a, b)
print("{} + {} = {}".format(a, b, num))

num = cal.sub(a, b)
print("{} - {} = {}".format(a, b, num))

num = cal.mul(a, b)
print("{} * {} = {}".format(a, b, num))

num = cal.div(a, b)
print("{} / {} = {}".format(a, b, num))
