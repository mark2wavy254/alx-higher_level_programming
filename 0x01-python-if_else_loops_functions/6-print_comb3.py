#!/usr/bin/python3
for m in range(0, 10):
    for n in range(m + 1, 10):
        if m < 8:
            print('{}{}, '.format(m, n), end='')
        elif m == 8 and n == 9:
            print('89')
