import _queue

class MaxQueue:
    # a queue that supports getMax() in O(1).
    def __init__(self):
        self.queue = _queue.Queue()
        self.maxHistory = _queue.Queue()

    def enqueue(self,x):
        self.queue.enqueue(x)
        
        if self.maxHistory.isEmpty() or self.maxHistory.peek() <= x:
            self.maxHistory = _queue.Queue()
            self.maxHistory.enqueue(x)
        else:
            self.maxHistory.enqueue(x)

    def dequeue(self):
        if self.queue.isEmpty(): return None

        item = self.queue.dequeue()
        if item == self.maxHistory.peek():
            self.maxHistory.dequeue()
        return item
    
    def getMax(self):
        return self.maxHistory.peek()
    
if __name__ == "__main__":
    mq = MaxQueue()
    mq.enqueue(1)
    mq.enqueue(2)
    mq.enqueue(3)
    print("max=",mq.getMax())
    print("deq", mq.dequeue())
    print("deq",mq.dequeue())
    mq.enqueue(0)
    mq.enqueue(8)
    mq.enqueue(0)
    print("deq",mq.dequeue())
    print("max=",mq.getMax())
    print("deq",mq.dequeue())
    print("deq",mq.dequeue())
    print("max=",mq.getMax())
    
