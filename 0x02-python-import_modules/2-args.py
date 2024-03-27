#!/usr/bin/python3

import sys

a = len(sys.argv) - 1

if a == 0:
    print("0 arguments. ")

print(f"Number of argments: {a}")

if a == 1:
    print("1 argument:")
    print(f"1: {sys.argv[0]}")

elif a > 1:
    print("{a} arguments:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
