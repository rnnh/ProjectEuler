#!/usr/bin/python3


def main():
    fibonacci = [1, 2]
    even_terms_sum = 0
    
    while fibonacci[-2] + fibonacci[-1] < 4000000:
        new_term = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(new_term)
    
    for term in fibonacci:
        if term % 2 == 0:
            even_terms_sum += term
    
    print(even_terms_sum)


if __name__ == "__main__":
    main()
