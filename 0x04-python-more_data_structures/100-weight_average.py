#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == "":
        return 0
    tot = sum(score * weight for score, weight in my_list)
    tot_weight = sum(weight for _, weight in my_list)
    return tot / tot_weight
