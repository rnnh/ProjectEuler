#!/usr/bin/python3


def find_collatz_seq_len(start_int):
    collatz_seq = [start_int]
    while collatz_seq[-1] != 1:
        if collatz_seq[-1] % 2 == 0:
            next_term = collatz_seq[-1] / 2
        else:
            next_term = 3 * collatz_seq[-1] + 1
        collatz_seq += [next_term]
    return len(collatz_seq)


def find_start_int_of_longest_collatz_seq(limit):
    collatz_seq_len = 0
    longest_collatz_seq_len = 0
    start_int_of_longest_collatz_seq = 0
    for n in xrange(1, limit):
        collatz_seq_len = find_collatz_seq_len(n)
        if collatz_seq_len > longest_collatz_seq_len:
            longest_collatz_seq_len = collatz_seq_len
            start_int_of_longest_collatz_seq = n
    return start_int_of_longest_collatz_seq


start_int_of_longest_chain = find_start_int_of_longest_collatz_seq(1000000)

print(start_int_of_longest_chain)
