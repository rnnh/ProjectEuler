#!/usr/bin/python3


def find_largest_prime_factor(n):
    while n % 2 == 0 and n / 2 > 1:
        n = n / 2
    for i in range(3, int((n**0.5) + 1), 2):
        while n % i == 0 and n / i != 1:
            n = n / i
    print(int(n))


if __name__ == "__main__":
    find_largest_prime_factor(600851475143)
