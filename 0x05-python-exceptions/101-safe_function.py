#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError) as r:
        print("Exception:", r, file=sys.stderr)
        return None
