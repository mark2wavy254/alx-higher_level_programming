#!/usr/bin/python3
for m in range(0, 100):
    print("{:02d}, ".format(int(m)), end='')
    if m == 99:
        print("", end='\n')
