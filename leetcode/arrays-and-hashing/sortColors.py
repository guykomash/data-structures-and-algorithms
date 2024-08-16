


def sortColors(nums):
    def exchange(i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


    l, r = 0, len(nums) - 1
    i = 0
    while i <= r:
        if nums[i] == 0:
            exchange(l, i)
            l += 1
        elif nums[i] == 2:
            exchange(i, r)
            r -= 1
            i -= 1 # check this cell again.
        i += 1
    