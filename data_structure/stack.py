import parent.child

class EmptyException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class Stack:

    def __init__(self):
        self.itemList = []

    def push(self, item):
        self.itemList.append(item)

    def pop(self):
        if(len(self.itemList) > 0):
            return self.itemList.pop()
        else:
            raise EmptyException

    def is_empty(self):
        return True if len(self.itemList) > 0 else False
    
    def size(self):
        return len(self.itemList)
