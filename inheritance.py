import ConfigParser, os

class First(object):
    def __init__(self):
        print "first"

class Second(First):
    def __init__(self):
        print "second"
class Third(First):
    def __init__(self):
        print "third"
class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print "that's it"

if __name__=="__main__":
    fo = Fourth()
    config = ConfigParser.ConfigParser()
    con = ConfigParser.ConfigParser()
    cn = ConfigParser.ConfigParser()
    print config
    print con
    print cn
