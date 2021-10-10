#!/usr/bin/python3

from math import sqrt


def find_triangle_number(n_factors: int):
    factors = []
    lower_half = []
    upper_half = []
    triangle = 1
    next_number = 2
    while len(factors) < n_factors:
        factors = []
        lower_half = []
        upper_half = []
        triangle += next_number
        next_number += 1
        for x in range(1, int(sqrt(triangle)) + 1):
            if triangle % x == 0:
                lower_half += [x]
        for y in lower_half:
            if triangle % y == 0:
                upper_half += [triangle / y]
        factors = list(set(lower_half + upper_half))
    return triangle


triangle_500 = find_triangle_number(500)
print(triangle_500)
