#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end='\n')
        return True
    except (TypeError, ValueError) as x:
        print("Exception:", x, file=sys.stderr)
        return False
