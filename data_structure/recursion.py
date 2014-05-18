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
    best.append(0)
    for i in (1, n):
        min = 10000
        for c in coins:
            if i - c  >= 0:
                print "i-c: %d" % (i-c)
                if best[i-c] < min:
                    min = best[i-c]
        if min != 10000:
            best.insert(i, min + 1)
        else:
            print "eo doi tien cho % duoc" % i
            best.insert(i, 10000)

    return best[n]

if __name__=="__main__":
    print exchangeMoney(5)
