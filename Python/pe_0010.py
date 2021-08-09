#!/usr/bin/python3

from math import sqrt


def segmented_sieve(limit: int):
    lower_limit = int(sqrt(limit))
    lower_segment_primes = find_primes(lower_limit)
    upper_segment_primes = []
    if lower_limit % 2 == 0:
        lower_limit += 1
    upper_segment = list(range(lower_limit, limit, 2))
    for n in upper_segment:
        is_prime = True
        for prime in lower_segment_primes:
            if n % prime == 0:
                is_prime = False
                break
        if is_prime:
            upper_segment_primes += [n]
    primes = lower_segment_primes + upper_segment_primes
    return primes


def find_primes(limit: int):
    primes = [2]
    n = 2
    while n < limit:
        is_prime = True
        n += 1
        for prime in primes:
            if n % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes += [n]
    return primes


primes_under_two_million = segmented_sieve(2000000)
print(sum(primes_under_two_million))
