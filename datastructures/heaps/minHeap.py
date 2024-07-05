class minHeap:
    def __init__(self, arr=[]):
        self.arr = arr[:]
        self.size = len(arr)
        self.buildMinHeap()
        print(self.arr)

    def extractMin(self):
        '''Time Complexity O(log n)'''
        if self.size == 0:
            raise Exception("cannot pop from empty heap")
        minValue = self.arr[0] 
        
        # ensure heap property
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.minHeapify(0)

        return minValue

    def getMin(self):
        '''Time Complexity O(1)'''
        if self.size == 0:
            return None
        return self.arr[0]
        
    def minHeapify(self, i):
        '''Time Complexity O(log n)'''
        '''maxHeapifty ensures that the subtree of i satisfies the heap property'''
        l = minHeap.leftChild(i)
        r = minHeap.rightChild(i)
        smallest  = i
        if l <= self.size - 1 and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r <= self.size - 1 and self.arr[r] < self.arr[smallest]:
            smallest  = r
        if smallest != i:
            tmp = self.arr[i] 
            self.arr[i] = self.arr[smallest]
            self.arr[smallest]  = tmp
            self.minHeapify(smallest)
    
    def buildMinHeap(self):
        ''' Time Complexity O(n) (using special formula)'''
        for i in range((len(self.arr)// 2 - 1), -1, -1):
            self.minHeapify(i)
        return self.arr

    def increaseKey(self, i, key):
        '''Time Complexity O(log n)'''
        if i < 0 or i >= self.size:
            raise Exception("increaseKey: i is out of bounds.")
        if key < self.arr[i]:
            # raise error?
            print("key < previous key")
        self.arr[i] = key
        while i > 0 and self.arr[minHeap.parent(i)] > self.arr[i]:
            tmp = self.arr[i]
            self.arr[i] = self.arr[minHeap.parent(i)] 
            self.arr[minHeap.parent(i)] = tmp
            i = minHeap.parent(i)
    
    def insert(self, key):
        self.arr.append(float("inf"))
        self.size += 1
        self.increaseKey(self.size - 1, key)
    
    @staticmethod
    def heapsort(arr):
        '''Time Complexity O(n log n)'''
        heap = minHeap(arr)
        i = len(arr) - 1
        while i >= 1:
            heap.arr[i] = heap.extractMin()
            i = i - 1
        return heap.arr

    @staticmethod
    def parent(i):
        return (i - 1) // 2
    
    @staticmethod
    def leftChild(i):
        return 2 * i + 1
    
    @staticmethod
    def rightChild(i):
        return 2 * i + 2
    
if __name__ == "__main__":
    nums = [4,1,3,2,16,9,10,14,8,7]
    sorted = minHeap.heapsort(nums)
    print(sorted)