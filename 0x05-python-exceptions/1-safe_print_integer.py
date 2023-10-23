#!/usr/bin/python3

def safe_print_integer(value):
    # Function that prints an integer with "{:d}".format().
    try:
        print("{:d}".format(int(value))
                , end='\n')
        return True
    except (ValueError, TypeError):
        return False
