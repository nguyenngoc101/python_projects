class Foo():
    x = 1
    _a = '_a'
    __b = '__b'
    def __init__(self):
        Foo.x += 1
        self.y = 'y'
        self._c = '_c'
        self.__d = 'd'
        z = 300
#f1 = Foo()
#print Foo.x
#f2 = Foo()
#print Foo.x
#print f2.x
#print f.x
#print f._a
#print f.y
#print f._c
#print f._Foo__d

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            return StopIteration()

sum(yrange(5))





















































