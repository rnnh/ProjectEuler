#! /usr/bin/python3


def find_largest_palindrome():
    largest_palindrome = 0
    for x in range(999, 99, -1):
        for y in range(999, 750, -1):
            product = x * y
            product_reversed = int(str(product)[::-1])
            if product > largest_palindrome and product == product_reversed:
                largest_palindrome = product
            if product < largest_palindrome and product == product_reversed:
                return largest_palindrome
    for x in range(999, 99, -1):
        for y in range(751, 99, -1):
            product = x * y
            product_reversed = int(str(product)[::-1])
            if product > largest_palindrome and product == product_reversed:
                largest_palindrome = product
            if product < largest_palindrome and product == product_reversed:
                return largest_palindrome


largest_three_digit_palindrome = find_largest_palindrome()
print(largest_three_digit_palindrome)
