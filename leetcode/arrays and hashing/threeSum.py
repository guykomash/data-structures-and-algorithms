
def threeSum(nums):
    res = []
    nums.sort()

    i = 0
    while i < len(nums):
        if i == 0 or nums[i] != nums[i - 1]:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # skip same l / r
                    while l < r and nums[l + 1] == nums[l]:
                        l = l + 1
                    while l < r and nums[r - 1] == nums[r]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
                elif curSum  < 0:
                    l = l + 1
                else:
                    r = r - 1    
        i = i + 1
    
    return res

def threeSumII(nums):
    # Using twosum.
    nums.sort()
    res = []
    for i,n in enumerate(nums):
        newNums = nums[i + 1:]
        val = twoSum(newNums, 0 - n)
        if val:
            for pair in val:
                triplet = [n, newNums[pair[0]],newNums[pair[1]]]
                triplet.sort()
                if triplet not in res:
                    res.append(triplet)
    return res




def twoSum(nums, target):
    if not nums: return None
    res = []
    solMap = {} # complement -> index
    for i in range(len(nums)):
        if target - nums[i] in solMap:
            res.append([solMap[target - nums[i]], i])
        else:
            solMap[nums[i]] = i
    return res


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4,0]
    res = threeSumII(nums)
    print(res)