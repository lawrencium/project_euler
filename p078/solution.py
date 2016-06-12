from util.solutiontimer import time_function

PERMUTATION_TABLE = {}


def internal_recursive_calculator(n):
    if n <= 1:
        return 0

    piles = 0
    for starting_pile in range(1, n / 2 + 1):
        piles += 1
        remainder = n - starting_pile
        # print 'internal', starting_pile, remainder
        piles += internal_recursive_calculator(remainder)
    return piles


def get_internal_permutations(remainder):
    if remainder in PERMUTATION_TABLE:
        return PERMUTATION_TABLE[remainder]

    permutations = internal_recursive_calculator(remainder)

    PERMUTATION_TABLE[remainder] = permutations
    print 'internal permutations for', remainder, 'was', permutations
    return permutations


def number_piles(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    piles = 1
    print n, 0
    for starting_pile in range(1, n / 2 + 1):
        piles += 1

        remainder = n - starting_pile
        print starting_pile, remainder
        internal_permutations = get_internal_permutations(remainder)
        piles += internal_permutations

    return piles


def main():
    print number_piles(5)


if __name__ == '__main__':
    time_function(main)
