#!/usr/bin/python3


def find_sum_square_difference(n):
    sum_of_integers = n * (n + 1)/2
    sum_of_squares = (n + 1) * (2 * n + 1) * n/6
    print(sum_of_integers ** 2 - sum_of_squares)


find_sum_square_difference(100)
