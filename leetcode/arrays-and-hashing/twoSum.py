

def twoSum(nums, target):
    map = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in map:
            return [map[needed], i]
        map[i] = i
    return [-1, -1]

if __name__ == "__main__":
    nums = [1,2,3,4]
    res = twoSum(nums,5)
    print(res)