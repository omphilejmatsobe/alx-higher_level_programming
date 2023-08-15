#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_a = (0, None)
    if sentence != "":
        tuple_a = (len(sentence), sentence[0])

    return (tuple_a)
