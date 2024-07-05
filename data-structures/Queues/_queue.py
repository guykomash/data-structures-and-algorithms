class LinkNode:
    def __init__(self, x):
        self.value = x
        self.next = self.prev = None

class Queue:
    def __init__(self):
        self.size = 0
        self.front, self.end = LinkNode(None), LinkNode(None)
        self.front.next, self.end.prev = self.end, self.front

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, x):
        prev, next = self.end.prev, self.end
        newNode = LinkNode(x)
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        
        prev, toRemove, next = self.front, self.front.next, self.front.next.next
        prev.next = next
        next.prev = prev
        self.size -= 1
        toRemove.next = toRemove.prev = None
        return toRemove.value
    
    def peek(self):
        if self.size == 0: return None
        return self.front.next.value
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    