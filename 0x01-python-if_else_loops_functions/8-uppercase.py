#!/usr/bin/python3
def uppercase(c):

    for cha in c:
        if ord(cha) >= 97 and ord(cha) <= 122:
            cha = chr(ord(cha) - 32)
            print("{}".format(cha), end="")
        else:
            print("{}".format(cha), end="")
    print("")
