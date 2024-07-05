class maxHeap:
    def __init__(self, arr=[]):
        self.arr = arr[:]
        self.size = len(arr)
        self.buildMaxHeap()

    def extractMax(self):
        '''Time Complexity O(log n)'''
        if self.size == 0:
            raise Exception("cannot pop from empty heap")
        maxValue = self.arr[0] 
        
        # ensure heap property
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.maxHeapify(0)

        return maxValue

    def getMax(self):
        '''Time Complexity O(1)'''
        if self.size == 0:
            return None
        return self.arr[0]
        
    def maxHeapify(self, i):
        '''Time Complexity O(log n)'''
        '''maxHeapifty ensures that the subtree of i satisfies the heap property'''
        l = maxHeap.leftChild(i)
        r = maxHeap.rightChild(i)
        largest  = i
        if l <= self.size - 1 and self.arr[l] > self.arr[largest]:
            largest = l
        if r <= self.size - 1 and self.arr[r] > self.arr[largest]:
            largest  = r
        if largest != i:
            tmp = self.arr[i] 
            self.arr[i] = self.arr[largest]
            self.arr[largest]  = tmp
            self.maxHeapify(largest)
    
    def buildMaxHeap(self):
        ''' Time Complexity O(n) (using special formula)'''
        for i in range((len(self.arr)// 2 - 1), -1, -1):
            self.maxHeapify(i)
        return self.arr

    def increaseKey(self, i, key):
        '''Time Complexity O(log n)'''
        if i < 0 or i >= self.size:
            raise Exception("increaseKey: i is out of bounds.")
        if key < self.arr[i]:
            # raise error?
            print("key < previous key")
        self.arr[i] = key
        while i > 0 and self.arr[maxHeap.parent(i)] < self.arr[i]:
            tmp = self.arr[i]
            self.arr[i] = self.arr[maxHeap.parent(i)] 
            self.arr[maxHeap.parent(i)] = tmp
            i = maxHeap.parent(i)
        return i
    
    def insert(self, key):
        self.arr.append(float("-inf"))
        self.size += 1
        index = self.increaseKey(self.size - 1, key)
        return index
    
    def delete(self, key):
        try:
            index = self.arr.index(key)
        except Exception as err:
            print(f"delete: key={key} not found.")
        self.increaseKey(index, float("-inf"))


    @staticmethod
    def heapsort(arr):
        '''Time Complexity O(n log n)'''
        heap = maxHeap(arr)
        i = len(arr) - 1
        while i >= 1:
            heap.arr[i] = heap.extractMax()
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
    h = maxHeap(nums)

    h.delete(2)
    print(h.arr)
    h.insert(2)
    print(h.arr)
