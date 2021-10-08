#!/usr/bin/python3

from math import sqrt


def find_triangle_number(n_factors: int):
    factors = []
    lower_half = []
    upper_half = []
    term = 1
    next_term = 2
    while len(factors) < n_factors:
        factors = []
        lower_half = []
        upper_half = []
        term += next_term
        next_term += 1
        for x in range(1, int(sqrt(term)) + 1):
            if term % x == 0:
                lower_half += [x]
        for y in lower_half:
            if term % y == 0:
                upper_half += [term / y]
        factors = list(set(lower_half + upper_half))
    return term


triangle_500 = find_triangle_number(500)
print(triangle_500)
