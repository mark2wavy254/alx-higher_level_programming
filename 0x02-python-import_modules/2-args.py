#!/usr/bin/python3

import sys

a = len(sys.argv) - 1

if a == 0:
    print("0 arguments. ")

if a == 1:
    print("1 argument:")
    print(f"1: {sys.argv[1]}")

elif a > 1:
    print(f"{a} arguments:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
