#! /usr/bin/python3


def prime_factorise(n):
    prime_factors = []
    while n % 2 == 0:
        n = n / 2
        prime_factors += [2]
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            prime_factors += [i]
            n = n / i
    if n > 2:
        prime_factors += [int(n)]
    return prime_factors


def find_lcm(list_of_integers):
    least_common_multiple = 1
    common_factors = []
    for n in list_of_integers:
        prime_factors = prime_factorise(n)
        for factor in prime_factors:
            if factor not in common_factors:
                common_factors += [factor]
            else:
                if prime_factors.count(factor) - common_factors.count(factor) > 0:
                    common_factors += [factor]
    for factor in common_factors:
        least_common_multiple = least_common_multiple * factor
    return least_common_multiple


one_to_twenty = list(range(1, 21))

lcm_one_to_twenty = find_lcm(one_to_twenty)

print(lcm_one_to_twenty)
