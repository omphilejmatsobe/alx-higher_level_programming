#!/usr/bin/python3

def safe_print_division(a, b):

   i = 0
   try:
       i = a / b
   except (ZeroDivisionError, ValueError, TypeError):
       i = None
    finally:
        print("{}".format(i))
        return (division)

