#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for elem in range(x):
            print("{}".format(my_list[elem]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
