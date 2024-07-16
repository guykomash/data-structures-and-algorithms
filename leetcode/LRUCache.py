class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node
        self.sz = 0

        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    # remove node from list
    def remove(self, node):
        # prev = node.prev
        # next = node.next
        # prev.next = next
        # next.prev = prev
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        # prev = self.mru.prev
        # prev.next = node
        # self.mru.prev = node
        # node.next = self.mru
        # node.prev = prev
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else: 
            # key does not exist
            if self.sz ==  self.cap:
                # remove from the list and delete the LRU from hashmap
                evict = self.lru.next
                self.remove(evict)
                del self.cache[evict.key]
                self.sz -= 1

            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            self.sz += 1



if __name__ == "__main__":
    cache = {}
    cache[5] = 4
    node = cache.get(5)

    if node is not None:
        print(node)
    
    n = cache.get(4)
    if n is None:
        print(" none")

