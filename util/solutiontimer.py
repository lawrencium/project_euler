import time

__author__ = 'lawrencechen'


def time_function(fxn):
    initial_time = time.time()
    fxn()
    print "\n< Finished in %f.2 seconds. >" % (time.time() - initial_time)
