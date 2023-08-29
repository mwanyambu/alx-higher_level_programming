#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for x in range(list_length):
        try:
                list_div = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            list_div = 0
        except TypeError:
            print("wrong type")
            list_div = 0
        except IndexError:
            print("out of range")
            list_div = 0
        finally:
            my_list_3.append(list_div)
    return my_list_3

