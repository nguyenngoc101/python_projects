def boyer_moore(t, p):
    n = len(t)
    m = len(p)
    s=0
    while s <= n-m:
        j = m
        while j>0 and t[s+j-1] == p[j-1]:
            j -= 1;
        if j==0:
            print "matching at %d " % s
            s += 1
        else:
            current = j
            while j>0 and t[s+current-1] != p[j-1]:
                j -= 1
            s += current - j

boyer_moore("ccac", "b")
