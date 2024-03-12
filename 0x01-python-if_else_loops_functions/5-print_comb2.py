#!/usr/bin/python3
for m in range(48, 58):
    for n in range(48, 58):
        print("{}{}, ".format(chr(m), chr(n)), end='')
    if m == 57 and n == 57:
        print("", end='\n')
