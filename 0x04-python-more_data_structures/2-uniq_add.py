#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    plus = 0
    for i in my_list:
        if i not in uniq:
            uniq.add(i)
            plus += i
    return plus

