import math
import random

EPSILON = 0.00000001
def equal(a, b): return abs(a - b) < EPSILON

class V:

    '''A mathematical vector of arbitrary number of scalar number elements.
    '''

    O = None
    X = None
    Y = None
    Z = None

    __slots__ = [ '_v', '_l' ]

    @classmethod
    def __constants__(cls):
        if V.O: return
        V.O = V() ; V.O._v = (0.,0.,0.) ; V.O._l = 0.
        V.X = V() ; V.X._v = (1.,0.,0.) ; V.X._l = 1.
        V.Y = V() ; V.Y._v = (0.,1.,0.) ; V.Y._l = 1.
        V.Z = V() ; V.Z._v = (0.,0.,1.) ; V.Z._l = 1.

    def __init__(self, *args):
        l = len(args)
        if not l:
            self._v = [0.,0.,0.]
            self._l = 0.
            return
        if l > 1:
            self._v = map(float, args)
            self._l = None
            return
        arg = args[0]
        if isinstance(arg, (list, tuple)):
            self._v = map(float, arg)
            self._l = None
        elif isinstance(arg, V):
            self._v = list(arg._v[:])
            self._l = arg._l
        else:
            arg = float(arg)
            self._v = [ arg ]
            self._l = arg

    def __len__(self):
        '''The len of a vector is the dimensionality.'''
        return len(self._v)

    def __list__(self):
        '''Accessing the list() will return all elements as a list.'''
        if isinstance(self._v, tuple): return list(self._v[:])
        return self._v[:]

    list = __list__

    def __getitem__(self, key):
        '''Vector elements can be accessed directly.'''
        return self._v[key]

    def __setitem__(self, key, value):
        '''Vector elements can be accessed directly.'''
        self._v[key] = value

    def __str__(self): return self.__repr__()
    def __repr__(self):
        return self.__class__.__name__ + repr(tuple(self._v))

    def __eq__(self, other):
        '''Vectors can be checked for equality.
        Uses epsilon floating comparison; tiny differences are still equal.
        '''
        for i in range(len(self._v)):
            if not equal(self._v[i], other._v[i]):
                return False
        return True
    def __cmp__(self, other):
        '''Vectors can be compared, returning -1,0,+1.
        Elements are compared in order, using epsilon floating comparison.
        '''
        for i in range(len(self._v)):
            if not equal(self._v[i], other._v[i]):
                if self._v[i] > other._v[i]: return 1
                return -1
        return 0

    def __pos__(self): return V(self)
    def __neg__(self):
        '''The inverse of a vector is a negative in all elements.'''
        v = V(self)
        for i in range(len(v._v)):
            v[i] = -v[i]
        v._l = self._l
        return v

    def __nonzero__(self):
        '''A vector is nonzero if any of its elements are nonzero.'''
        for i in range(len(self._v)):
            if self._v[i]: return True
        return False

    def zero(self):
        '''A vector is zero if none of its elements are nonzero.'''
        return not self.__nonzero__()

    @classmethod
    def random(cls, order=3):
        '''Returns a unit vector in a random direction.'''
        # distribution is not without bias, need to use polar coords?
        v = V(range(order))
        v._l = None
        short = True
        while short:
            for i in range(order):
                v._v[i] = 2.0*random.random() - 1.0
                if not zero(v._v[i]): short = False
        return v.normalize()

    # Vector or scalar addition.
    def __add__(self, other): return self.__class__(self).__iadd__(other)
    def __radd__(self, other): return self.__class__(self).__iadd__(other)
    def __iadd__(self, other):
        '''Vectors can be added to each other, or a scalar added to them.'''
        if isinstance(other, V):
            if len(other._v) != len(self._v):
                raise ValueError, 'mismatched dimensions'
            for i in range(len(self._v)):
                self._v[i] += other._v[i]
        else:
            for i in range(len(self._v)):
                self._v[i] += other
        self._l = None
        return self

    # Vector or scalar subtraction.
    def __sub__(self, other): return self.__class__(self).__isub__(other)
    def __rsub__(self, other): return (-self.__class__(self)).__iadd__(other)
    def __isub__(self, other):
        '''Vectors can be subtracted, or a scalar subtracted from them.'''
        if isinstance(other, V):
            if len(other._v) != len(self._v):
                raise ValueError, 'mismatched dimensions'
            for i in range(len(self._v)):
                self._v[i] -= other._v[i]
        else:
            for i in range(len(self._v)):
                self._v[i] -= other
        self._l = None
        return self

    # Cross product or magnification.  See dot() for dot product.
    def __mul__(self, other):
        #if isinstance(other, M): return other.__rmul__(self)
        return self.__class__(self).__imul__(other)
    def __rmul__(self, other):
        # The __rmul__ is called in scalar * vector case; it's commutative.
        return self.__class__(self).__imul__(other)
    def __imul__(self, other):
        '''Vectors can be multipled by a scalar. Two 3d vectors can cross.'''
        if isinstance(other, V):
            self._v = self.cross(other)._v
        else:
            for i in range(len(self._v)):
                self._v[i] *= other
        self._l = None
        return self

    def __div__(self, other): return self.__class__(self).__idiv__(other)
    def __rdiv__(self, other):
        raise TypeError, 'cannot divide scalar by non-scalar value'
    def __idiv__(self, other):
        '''Vectors can be divided by scalars; each element is divided.'''
        other = 1.0 / other
        for i in range(len(self._v)):
            self._v[i] *= other
        self._l = None
        return self

    def cross(self, other):
        '''Find the vector cross product between two 3d vectors.'''
        if len(self._v) != 3 or len(other._v) != 3:
            raise ValueError, 'cross multiplication only for 3d vectors'
        p, q = self._v, other._v
        r = [ p[1] * q[2] - p[2] * q[1],
              p[2] * q[0] - p[0] * q[2],
              p[0] * q[1] - p[1] * q[0] ]
        return V(r)

    def dot(self, other):
        '''Find the scalar dot product between this vector and another.'''
        s = 0
        for i in range(len(self._v)):
            s += self._v[i] * other._v[i]
        return s

    def __mag(self):
        if self._l is not None:
            return self._l
        m = 0
        for i in range(len(self._v)):
            m += self._v[i] * self._v[i]
        self._l = math.sqrt(m)
        return self._l

    def magnitude(self, value=None):
        '''Find the magnitude (spatial length) of this vector.
        With a value, return a vector with same direction but of given length.
        '''
        mag = self.__mag()
        if value is None: return mag
        if zero(mag):
            raise ValueError, 'Zero-magnitude vector cannot be scaled.'
        v = self.__class__(self)
        v.__imul__(value / mag)
        v._l = value
        return v

    def dsquared(self, other):
        m = 0
        for i in range(len(self._v)):
            d = self._v[i] - other._v[i]
            m += d * d
        return m

    def distance(self, other):
        '''Compare this vector with another, for distance.'''
        return math.sqrt(self.dsquared(other))

    def normalize(self):
        '''Return a vector with the same direction but of unit length.'''
        return self.magnitude(1.0)

    def order(self, order):
        '''Remove elements from the end, or extend with new elements.'''
        order = int(order)
        if order < 1:
            raise ValueError, 'cannot reduce a vector to zero elements'
        v = V(self)
        while order < len(v._v):
            v._v.pop()
        while order > len(v._v):
            v._v.append(1.0)
        v._l = None
        return v