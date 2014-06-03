#def fibonacci():
#    a, b = 0, 1
#    while True:
#        yield a
#        a, b = b, a+b
#
#def trivial_sum(a):
#    for i in range(1,len(a)):
#            b[i] = a[i] + b[i-1]
#    return b
#f = fibonacci()
#for i, f in enumerate(f):
#    print i, f
#    if i >= 10: break
#print trivial_sum([1,2,3,4])
#print cumulative_sum([1,2,3,4,5,6])
#def get_value():
#    for i in range(1):
#        yield i
#a=[1,2]
#for x in a:
#    print x
#    a.append(2)

class MyRange():

    def __init__(self,input_list):
        self._arr = input_list
        self._count = 0
        self._n = len(input_list)

    def __iter__(self):
        return self

    def next(self):
        if self._count < self._n:
            i = self._count
            v = self._arr[self._count]
            self._count += 1
            return i,v
        else:
            raise StopIteration()
#ra = MyRange([1,2,3,4,5])
#print ra.next()
#print ra.next()
#print ra.next()
#print ra.next()
#print ra.next()
a = ["a", "b", "c"]
for i,c in MyRange(a):
    print i,c
