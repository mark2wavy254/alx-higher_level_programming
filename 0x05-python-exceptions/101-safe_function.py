#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (RuntimeError, ZeroDivisionError, TypeError, IndexError, ValueError) as r:
        print("Exception:", r, file=sys.stderr)
        return None
