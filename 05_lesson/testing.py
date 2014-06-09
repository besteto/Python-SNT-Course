# testing - useful routines for running tests

'''

A few useful routines for running unit tests.

SYNOPSIS

    import testing ; from testing import *

    def my_routine(number):
        return { 'one': 1, 'two': 2, 'three': 3}[number]

    def __test__():
        __ok__( my_routine("three"), 3 )
        __report__()

AUTHOR

    Ed Halley (ed@halley.cc) 17 October 2007

'''

__all__ = [ '__ok__', '__time__', '__report__' ]

#----------------------------------------------------------------------------

__tests = 0
__fails = 0

def __tests__(): return __tests
def __fails__(): return __fails

def __ok__(test, expect=True, message=''):
    global __tests
    global __fails
    __tests += 1
    if message: message = ' (%s)' % message
    if (test != expect):
        __fails += 1
        print "Test %d%s: [FAIL] expected %s but got %s" % \
              (__tests, message, repr(expect), repr(test))
    else:
        print "Test %d%s: [OK] %s" % \
              (__tests, message, repr(expect))

def __time__(name=None, setup='pass', stmt='pass'):
    if name is None: name = stmt
    import timeit
    timer = timeit.Timer(stmt, setup)
    number = 1000000
    timings = timer.repeat(repeat=3, number=number)
    sec = min(timings)
    desc = "%.2f us/run" % (1e6*sec/number)
    print "%18s : %s" % (desc, name)

def __report__():
    global __tests
    global __fails
    if __fails > 0:
        print 'Total of %d failed tests out of %d tests.' % \
              (__fails, __tests)
    else:
        print 'Total of %d tests.  Success.' % __tests

#----------------------------------------------------------------------------

if __name__ == '__main__':
    raise Exception, \
        'This module is not a stand-alone script.  Import it in a program.'