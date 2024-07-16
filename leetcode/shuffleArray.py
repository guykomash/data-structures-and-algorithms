import random

class ShuffleArray:
    def __init__(self, nums):
        self.nums = nums
        
    def reset(self):
        return self.nums

    def shuffle(self):
        # low to high shuffle
        nums = self.backup[:]
        n = len(nums)
        i = 0
        while i < n - 1:
            j = random.randint(i, n - 1)
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        return nums


    def FYshuffle(self):
        shuffled = self.nums.copy()
        i = len(shuffled) - 1
        while i >= 0:
            # store current number.
            j = random.randint(0,i)
            # if i =j . continue
            if i != j:
                temp = shuffled[i]
                shuffled[i] = shuffled[j]
                shuffled[j] = temp
            i -= 1
        return shuffled

    def choogiShuffle(self):
        shuffled = []
        
        indeces = ["X" for _ in range(len(self.nums))]
        for i in range(len(self.nums)):
            chosenIndex = random.randint(0, len(self.nums) - 1)
            while indeces[chosenIndex] is None:
                chosenIndex = random.randint(0, len(self.nums) - 1)
            indeces[chosenIndex] = None
            shuffled.append(self.nums[chosenIndex])
        return shuffled
        
if __name__ == "__main__":
    shuffleSystem = ShuffleArray([1,2,3,4])
    # # shuf1 = shuffleSystem.FYshuffle()
    # shuf2 = shuffleSystem.choogiShuffle()
    # print(shuf2) 
    shuf = shuffleSystem.FYshuffle()
    print(shuf)