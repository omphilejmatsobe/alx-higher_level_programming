#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    stateList = []

    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            stateList.append(True)
        else:
            stateList.append(False)

    return (stateList)
