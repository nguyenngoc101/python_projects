def select(k,n):
    if k == 0 and n >= 0:
        return 1
    if k > 0 and n==k:
        return 1
    if k > n :
        return 0
    return (giaiThua(n)/(giaiThua(n-k)*giaiThua(k)))

def giaiThua(n):
    if n==1:
        return 1
    else:
        return n*giaiThua(n-1)

if __name__=="__main__":
    inputs = raw_input('input: ')
    numbers = map(int, inputs.split())
    n,m,x=numbers[0],numbers[1],numbers[2]
    first_part = x
    secon_part = m-x
    total = 0
    ok1 = 0
    ok2 = 0
    for k in range(1,n+1):
        ok1 = select(k-1,x)
        print "k-1: %d, x: %d" % (k-1,x)
        print "ok1 %d" % ok1
        if ok1:
             ok2 = select(n-k-1,m-x)
             if ok2:
                 total = ok1 + ok2
    print total
