class Node:
    def __init__(self, item):
        self.item  = item
        self.next = None

    def getNext(self):
        return  self.next;

    def setNext(self, node):
        self.next = node

    def getItem(self):
        return self.item

    def setItem(self, item):
        self.item = item;

class LinkedList:
    def __init__(self):
        self.head = None
        self.first = None

    def append(self, item):
        if self.head == None:
            self.first = item
            self.head = item
        else:
            self.head.setNext(item)
            self.head =  item

    def remove(self, item):
        temp = self.first
        while True:
            if(temp )
        pass

    def search(self, item):
        pass

    def isEmpty(self):
        return True if self.size() == 0 else False

    def size(self):
        if self.head is None:
            return 0

        temp = self.first
        counter = 1
        while temp != self.head:
            temp = temp.getNext()
            counter += 1
        return counter

    def insert(self, position, item):
        pass

    def pop(self):
        pass

    def pop(self, position):
        pass

if __name__=="__main__":
    myList = LinkedList()
    print "size: %d" % myList.size()
    node = Node(1)
    myList.append(node)
    node = Node(2)
    myList.append(node)
    node = Node(2)
    myList.append(node)
    print "size: %d" % myList.size()

