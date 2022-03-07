#!/usr/bin/python3


def find_factorial(n: int):
    factorial = 1
    while n != 1:
        factorial = factorial * n
        n = n - 1
    return(factorial)


def count_paths(grid_size: int):
    numerator = find_factorial(grid_size * 2)
    denominator = find_factorial(grid_size) * find_factorial(grid_size)
    paths = int(numerator / denominator)
    return(paths)


path_count_20_grid = count_paths(20)

print(path_count_20_grid)
