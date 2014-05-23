def convertBinary(integer):
    if integer == 0 or integer == 1:
        return str(integer)
    else:
        return  convertBinary(integer/2) + str(integer % 2)

def towerOfHanoi(n, a, b, c):
    if n == 1:
        print "move from %s to %s" %(a, c)
    else:
        towerOfHanoi(n-1, a, c, b)
        print "move from %s to %s" %(a, c)
        towerOfHanoi(n-1, b, a, c)
coins =  [1, 2, 5, 10, 25]
best = []
print  best
def exchangeMoney(n):
    best = [10000]*n
    best.insert(0, 0)
    coin = None
    exchanges = [[]]*(n+1)
    for i in range(1, n+1):
        min = 10000
        exchanges.insert(i, [])
        for c in [x in coins if i-x >= 0]:
            if best[i-c] < min:
                min = best[i-c]
                coin = c
        if min != 10000:
            best.insert(i, min + 1)
            exchanges[i].extend(exchanges[i-coin])
            exchanges[i].extend([coin])
        else:
            best.insert(i, 10000)
        print "i= %d" % i
        print "exchanges[%d]: %s" % (i, exchanges[i])
        print "best[%d]: %s" % (i, best[i])


if __name__=="__main__":
    exchangeMoney(9)
