#!/usr/bin/python3

import sys

def add_args(a):
    return sum(int(b) for b in a)

if __name__ == "__main__":
    total = add_args(sys.argv[1:])
    print(total)
