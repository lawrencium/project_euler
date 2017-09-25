from problems.p114.block_combination import BlockCombinationCounter
from problems.util.solutiontimer import time_function


def main():
    threshold = 1000000

    m = 50
    n = 50

    while True:
        if BlockCombinationCounter(m, n).count() > threshold:
            print n
            return

        n += 1


if __name__ == '__main__':
    time_function(main)
