from problems.p114.block_combination import BlockCombinationCounter
from problems.util.solutiontimer import time_function


def main():
    print BlockCombinationCounter(3, 50).count()


if __name__ == '__main__':
    time_function(main)
