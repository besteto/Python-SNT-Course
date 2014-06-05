from vector import  *

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

print 'Testing V vector class...'

# structural construction
__ok__(V.O is not None, True)
__ok__(V.O._v is not None, True)
__ok__(V.O._v, (0., 0., 0.)) ; __ok__(V.O._l, 0.)
__ok__(V.X._v, (1., 0., 0.)) ; __ok__(V.X._l, 1.)
__ok__(V.Y._v, (0., 1., 0.)) ; __ok__(V.Y._l, 1.)
__ok__(V.Z._v, (0., 0., 1.)) ; __ok__(V.Z._l, 1.)
a = V(3., 2., 1.) ; __ok__(a._v, [3., 2., 1.])
a = V((1., 2., 3.)) ; __ok__(a._v, [1., 2., 3.])
a = V([1., 1., 1.]) ; __ok__(a._v, [1., 1., 1.])
a = V(0.) ; __ok__(a._v, [0.]) ; __ok__(a._l, 0.)
a = V(3.) ; __ok__(a._v, [3.]) ; __ok__(a._l, 3.)

# constants and direct comparisons
__ok__(V.O, V(0.,0.,0.))
__ok__(V.X, V(1.,0.,0.))
__ok__(V.Y, V(0.,1.,0.))
__ok__(V.Z, V(0.,0.,1.))

# formatting and elements
__ok__(repr(V.X), 'V(1.0, 0.0, 0.0)')
__ok__(V.X[0], 1.)
__ok__(V.X[1], 0.)
__ok__(V.X[2], 0.)

# simple addition
__ok__(V.X + V.Y, V(1.,1.,0.))
__ok__(V.Y + V.Z, V(0.,1.,1.))
__ok__(V.X + V.Z, V(1.,0.,1.))

# didn't overwrite our constants, did we?
__ok__(V.X, V(1.,0.,0.))
__ok__(V.Y, V(0.,1.,0.))
__ok__(V.Z, V(0.,0.,1.))

a = V(3.,2.,1.)
b = a.normalize()
__ok__(a != b)
__ok__(a == V(3.,2.,1.))
__ok__(b.magnitude(), 1)
b = a.magnitude(5)
__ok__(a == V(3.,2.,1.))
__ok__(b.magnitude(), 5)
__ok__(equal(b.dsquared(V.O), 25))

a = V(3.,2.,1.).normalize()
__ok__(equal(a[0], 0.80178372573727319))
b = V(1.,3.,2.).normalize()
__ok__(equal(b[2], 0.53452248382484879))
d = a.dot(b)
__ok__(equal(d, 0.785714285714), True)

__ok__(V(2., 2., 1.) * 3, V(6, 6, 3))
__ok__(3 * V(2., 2., 1.), V(6, 6, 3))
__ok__(V(2., 2., 1.) / 2, V(1, 1, 0.5))

v = V(1,2,3)
w = V(4,5,6)
__ok__(v.cross(w), V(-3,6,-3))
__ok__(v.cross(w), v*w)
__ok__(v*w, -(w*v))
__ok__(v.dot(w), 32)
__ok__(v.dot(w), w.dot(v))

__ok__(zero(angle(V(1,1,1), V(2,2,2))), True)
__ok__(equal(90.0, degrees(angle(V(1,0,0), V(0,1,0)))), True)
__ok__(equal(180.0, degrees(angle(V(1,0,0), V(-1,0,0)))), True)

__ok__(equal(  0.0, degrees(track(V( 1, 0)))), True)
__ok__(equal( 90.0, degrees(track(V( 0, 1)))), True)
__ok__(equal(180.0, degrees(track(V(-1, 0)))), True)
__ok__(equal(270.0, degrees(track(V( 0,-1)))), True)

__ok__(equal( 45.0, degrees(track(V( 1, 1)))), True)
__ok__(equal(135.0, degrees(track(V(-1, 1)))), True)
__ok__(equal(225.0, degrees(track(V(-1,-1)))), True)
__ok__(equal(315.0, degrees(track(V( 1,-1)))), True)