import sys
import os


# # Adjust the path to the project root
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from datastructures.trees import display_tree


from math import log, ceil

class RangeSumQueryImmutable:
    def __init__(self, nums):
        self.sumLeft = [0] * len(nums)
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            self.sumLeft[i] = curSum

    def sumRange(self, left, right):
        right = self.sumLeft[right]
        left = self.sumLeft[left - 1] if left > 0 else 0
        return right - left


class SegTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = self.right = None

class RangeSumQueryMutable:
    def __init__(self, nums):
        self.root = self.buildTree(nums, 0, len(nums) - 1)
        # display_tree(self.root)

    # build tree.
    def buildTree(self, nums, start, end):
        if start > end: return None
        
        root = SegTreeNode(start, end)

        if start == end:
            # leaf
            root.sum = nums[start]
        else:
            mid = start + (end - start ) // 2
            root.left = self.buildTree(nums, start, mid)
            root.right = self.buildTree(nums, mid + 1, end)
            root.sum = root.left.sum + root.right.sum
        return root


    def update(self, index: int, val: int) -> None:
        
        def updateRec(root, index, val):
            if root.start == root.end == index:
                root.sum = val
                return
            
            mid = root.start + (root.end - root.start) // 2
            if index <= mid:
                updateRec(root.left, index, val)
            else:
                updateRec(root.right, index, val)

            root.sum = root.left.sum + root.right.sum
            
        updateRec(self.root, index, val)
        print("Update complete")
        # display_tree(self.root)

    def sumRange(self, left: int, right: int) -> int:
        if left < self.root.start or right > self.root.end: return None

        def sumRangeDFS(root, start, end):
            # print(f"sumRangeDFS {start} {end} ")
            # found exact range in this node
            if root.start == start and root.end == end:
                return root.sum
            
            mid = root.start + (root.end - root.start) // 2
            # print(f"mid = {mid}")
            if end <= mid:
                # the sum is in the left subtree
                return sumRangeDFS(root.left, start, end)
            elif start > mid:
                return sumRangeDFS(root.right, start, end)
            else:
                # need to combine start -> mid  of left and mid -> end of right
                return sumRangeDFS(root.left, start, mid) + sumRangeDFS(root.right, mid + 1, end) 

        return sumRangeDFS(self.root, left, right)

class RangeSumQueryMutableII:
    def __init__(self, nums):
        self.heap = self.build(nums)


    def build(self,nums):
        n = len(nums)
        heap = [0] * (2*n)
        l = 0
        r = n
        while l < n:
            heap[r] = nums[l]
            l += 1
            r += 1
        
        i = n - 1
        while i >= 0:
            # i is parent
            left = heap[2 * i + 1] if (2*i + 1) < 2 * n else 0
            right= heap[2 * i + 2] if (2 * i + 2) < 2 * n else 0
            print(f"i={i} left={left} right={right}")
            heap[i] = left + right
            i -= 1
        print(f"builded {heap}")
        return heap
        



    def update(self, index, val):
        pass
    def sumRange(self, left, right):
        pass

class RangeSumQueryPFT:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.h = ceil(log(self.n,2))
        self.sz = (2 ** (self.h + 1)) - 1
        print(f"self.sz = {self.sz}")
        self.segTree = [None] * (self.sz)
        self.buildTree(0,0,self.n - 1)
    
    def buildTree(self, node, start, end):
        # print(f"buildTree = {node},{start},{end}")
        if start == end:
            self.segTree[node] = self.nums[start]
            return
        
        mid = start + (end - start ) // 2
        self.buildTree(2 * node + 1, start, mid)
        self.buildTree(2 * node + 2, mid + 1, end)
        self.segTree[node] = self.segTree[2 * node + 1] + self.segTree[2 * node + 2]
    
    def update(self, index, value):
        if index < 0 or index >= self.n: return f"Error: {index} is not valid index, choose in range [0 - {self.n - 1}]"
        # self.updateDFS(0, 0, self.n - 1, index, value)
        self.updateIter(index, value)
        return "updated."
    
    def updateDFS(self, node, start, end, index,value):
        if start == end:
            self.segTree[node] = value
            # nums[index] = value
            # print(f"start==end=={start}, node={node}")
            # print(f"u {self.segTree}")
        else:
            mid = start + (end - start) // 2
            if index <= mid:
                # index is in left sub stree
                self.updateDFS(2 * node + 1, start, mid, index, value)
            else:
                self.updateDFS(2 * node + 2, mid + 1, end, index, value)

            # returned to current node
            self.segTree[node] = self.segTree[2 * node + 1] + self.segTree[2 * node + 2]
            print(self.segTree)

    def getTreeIndex(self, index):
            cur =  self.sz - (2 ** (self.h)) + index
            while self.segTree[cur] is None:
                cur = (cur - 1) // 2
            return cur
    
    def updateIter(self, index, value):
        cur = self.getTreeIndex(index)
        self.segTree[cur] = value
        while cur > 0:
            # go to parent
            cur = cur // 2
            self.segTree[cur] = self.segTree[2 * cur + 1] + self.segTree[2 * cur + 2]

    def sumRange(self, left, right):
        # return self.sumRangeDFS(0, 0, self.n - 1, left, right)
        return self.sumRangeIter(left, right)
    
    def sumRangeDFS(self, node,start, end, left, right):
        print(f"sumRangeDFS = {node},{start},{end},{left},{right}")
        if left > right:
            return 0
        if end < start: return 0 
        if node >= self.sz:
            return 0
        
        if start == end:
            return self.segTree[node]
        
        mid = start + (end - start ) // 2

        if right <= mid:
            # sum is in left sub tree
           return self.sumRangeDFS(2 * node + 1, start, mid, left, right)
        elif mid < left:
            # sum is in right sub tree
            return self.sumRangeDFS(2 * node + 2, mid + 1, end, left, right)
        else:
            # need both subtrees.
            left =  self.sumRangeDFS(2 * node + 1, start, mid, left, mid)
            right = self.sumRangeDFS(2 * node + 2, mid + 1, end, mid + 1, right)
            
            return left + right

    def sumRangeIter(self,left, right):
        curR = self.getTreeIndex(right)
        curL = self.getTreeIndex(left)
        print(f"starting = {curL}, {curR}")
        total = 0    

        while curL !=  curR:
            # print(f"{curL == curR}")
            if curR % 2 == 1:
                # the right side is left child. skip its parent, take him instead
                total += self.segTree[curR]
                print(f"new total = {total} , curR={curR}")
                # curR = curR - 1

            if curL % 2 == 0:
                # the left node is a right child. skip the parent(holds left child.)
                total += self.segTree[curL]
                print(f"new total = {total}, curL={curL}")
                # curL = curL + 1


            if curL == curR == 0:
                break
            # if curL > curR: 
            #     break
            # else:
            print(f"finished = {curL} , {curR}")
            curR = (curR - 1) // 2
            curL = (curL - 1) // 2
            if curL < 0 or curR < 0:
                break

        return total

if __name__ == "__main__":
    r = RangeSumQueryMutable([1,2,3,4])
    # print(r.nums)
    # r.update(2,22)
    # r.update(4,22)

    print(r.sumRange(0,3)) # 10
    print(r.sumRange(0,2)) # 6
    print(r.sumRange(0,1)) # 3
    print(r.sumRange(0,0)) # 1
    print(r.sumRange(1,3)) # 9
    print(r.sumRange(2,3)) # 7
    
