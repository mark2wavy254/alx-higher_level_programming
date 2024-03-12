#!/usr/bin/python3
for m in range(48, 57):
    for n in range(49, 58):
        print("{}{}, ".format(chr(m), chr(n)), end='')
        if m == 56 and n == 57:
            print("{}{}".format(chr(m), chr(n)), end='\n')
