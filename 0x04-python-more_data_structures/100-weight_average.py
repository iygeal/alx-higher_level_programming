#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    score_sum = 0
    weight_sum = 0

    for score, weight in my_list:
        score_sum += score * weight
        weight_sum += weight
    weighted_average = score_sum / weight_sum
    return weighted_average
