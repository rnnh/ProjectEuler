#!/usr/bin/python3


def find_pythagorean_triplet_product():
    a = 0
    b = 1
    c = 2
    while a + b + c != 1000:
        a += 1
        b = (1000 ** 2 - 2000 * a) / (2000 - 2 * a)
        if isinstance(b, float) or a > b:
            break
        c = (1000 ** 2 + 2 * b * (b - 1000)) / (2000 - 2 * b)
        if isinstance(c, float) or b > c:
            break
    return a * b * c


pythagorean_triplet_product = find_pythagorean_triplet_product()

print(pythagorean_triplet_product)
