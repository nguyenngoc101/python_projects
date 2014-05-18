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
            raise EmptyException("Empty Stack Error")

    def is_empty(self):
        return True if self.size() == 0 else False

    def size(self):
        return len(self.itemList)

def convertBinary(int_input):
    converted_binary=""
    stack = Stack()
    while True:
        # stack.push(0) if int_input % 2 else stack.push(1)
        stack.push((int_input % 2))
        int_input /= 2
        if int_input < 1:
            break
    while not stack.is_empty():
        converted_binary += str(stack.pop())

    return  converted_binary

