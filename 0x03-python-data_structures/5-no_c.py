#!/usr/bin/python3

def no_c(my_string):
    track = ""
    for i in range(len(my_string)):
        if my_string[i] != "C" and my_string[i] != "c":
            track += my_string[i]
    return (track)


