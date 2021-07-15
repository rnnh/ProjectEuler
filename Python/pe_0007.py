#!/usr/bin/python3


def find_nth_prime(n):
    primes = [2]
    candidate = 2
    is_prime = True
    while len(primes) <= n - 1:
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes += [candidate]
        candidate += 1
        is_prime = True
    return primes[-1]


prime_10001 = find_nth_prime(10001)

print(prime_10001)
