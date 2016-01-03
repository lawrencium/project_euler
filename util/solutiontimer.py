import time

__author__ = 'lawrencechen'


def time_function(fxn):
    initial_time = time.time()
    fxn()
    print "\n< Finished in {0:.4f} seconds. >".format(time.time() - initial_time)
