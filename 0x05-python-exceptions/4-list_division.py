#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    _list = []
    for i in range(0, list_length):
        try:
            i = my_list1[i] / my_list2[i]
        except TypeError:
            print("wrong type")
            i = 0
        except ZeroDivisionError:
            print("division by 0")
            i = 0
        except IndexError:
            print("out of range")
            i = 0
        finally:
            _list.append(i)
    return (_list)
