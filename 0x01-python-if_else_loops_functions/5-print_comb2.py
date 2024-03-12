#!/usr/bin/python3
for m in range(0, 100):
    if m < 10:
        print("0{}, ".format(int(m)), end='')
    else:
        print("{}, ".format(int(m)), end= '')
    if m == 99:
        print("", end='\n')
