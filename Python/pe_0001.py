#!/usr/bin/python3


def main():
    # Find the sum of all the multiples of 3 or 5 below 1000

    multiples = []

    for i in range(1, 1000):
        if i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)

    print(sum(multiples))


if __name__ == "__main__":
    main()
