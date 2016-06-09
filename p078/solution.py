from util.solutiontimer import time_function

PERMUTATION_DICTIONARY = {}


def recursive_calculator(n):
    # if n <= 1:
    #     return n
    #
    # piles = 0
    # piles += n / 2 + 1
    # for i in range(n / 2 + 1):
    #     remainder = n - i
    #     piles += recursive_calculator(i)
    #     piles += recursive_calculator(remainder)

    if n == 1:
        return 1
    elif n == 0:
        return 0


def calculate_number_piles(n):
    if n == 1:
        return 1


def number_piles(n):
    if n in PERMUTATION_DICTIONARY:
        return PERMUTATION_DICTIONARY[n]
    else:
        calculate_number_piles(n)


def main():
    pass


if __name__ == '__main__':
    time_function(main)
