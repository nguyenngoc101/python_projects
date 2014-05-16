import graphics

class myClass:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name


if __name__=="__main__":
    cl = myClass("ngoc aaaaaaaaaaaaaaaa")
    print cl.name 
