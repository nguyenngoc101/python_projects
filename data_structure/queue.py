class EmptyQueueError(Exception):
    def __init__(self, message):
        Exception.__init__(self,message)

class Queue:

    def __init__(self):
        self.queue = []

    def dequeue(self):
        if self.size() > 0 :
            return self.queue.pop(0)
        else:
            raise EmptyQueueError("Empty Queue Error")

    def enqueue(self, item):
        self.queue.append(item)

    def isEmpty(self):
        return True if self.queue == [] else False

    def size(self):
        return len(self.queue)

if __name__=="__main__":
    print "Test Queue"
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print "size: %d" % queue.size()
    print queue.dequeue()
    print queue.dequeue()
    print "is empty %s" % queue.isEmpty()
    print queue.dequeue()
    print "is empty %s" % queue.isEmpty()
