import math

from problems.p121.disk_game import DiskGame
from problems.util.solutiontimer import time_function

__author__ = 'lawrencechen'

ROUNDS_PER_GAME = 15


def main():
    disk_game = DiskGame()

    win_probability = disk_game.win_probability(ROUNDS_PER_GAME, 1, 0)
    print 'Win probability for Disk Game with %i rounds per game is %f' % (ROUNDS_PER_GAME, win_probability)
    print 'Maximum payout is %i' % math.floor(1 / win_probability)


if __name__ == '__main__':
    time_function(main)
