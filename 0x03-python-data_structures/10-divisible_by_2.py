#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) < 0:
        return None
    else:
        lst = []
        for i in my_list:
            if i % 2 == 0:
                lst.append(True)
            else:
                lst.append(False)
        return lst
