
def subsets(nums):
    stack = []
    res = []
    def f(i):
        if i >= len(nums):
            res.append(stack[:]) 
            return

        f(i + 1)
        stack.append(nums[i])
        f(i + 1)
        stack.pop()

    f(0)
    return res       


if __name__ == "__main__":
   nums = [1,2,3]
   res = subsets(nums)
   print(res)