def ThangTD(a,b):
    if a >= 2 and b>=2:
        a -= 2
        b -= 2
        return True,a,b
    if a >= 1 and b >= 12:
        a -= 1
        b -= 12
        return True,a,b
    if  b >= 22:
        b -= 22
        return True,a,b
    return False,a,b

def DungNQ(a,b):
   if b >= 22:
       b -= 22
       return True,a,b
   if b >=12 and a>=1:
       a -= 1
       b -= 12
       return True,a,b
   if b >= 2 and a >= 2:
       a -= 2
       b -=2
       return True,a,b
   return False,a,b

if __name__=="__main__":
    coins = raw_input('input: ')
    numbers = map(int, coins.split())
    res = [True, numbers[0], numbers[1]]
    while True:
        res = ThangTD(res[1], res[2])
        if not res[0]:
            print "DungNQ"
            break
        res = DungNQ(res[1], res[2])
        if not res[0]:
            print "ThangTD"
            break
