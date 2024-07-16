def productExceptSelf(nums):
    # from left to right:
    prods = [1] * len(nums)
    leftProd = 1
    i = 0
    while i < len(nums):
        prods[i] = leftProd * prods[i]
        leftProd *= nums[i]
        i += 1

    rightProd = 1
    i -= 1
    while i >= 0:
        prods[i] = rightProd * prods[i]
        rightProd *= nums[i]
        i -= 1
    return prods

def productExceptSelfII(nums):
    n = len(nums)
    p = 1
    prods = [0] * n
    for i in range(n):
        prods[i] = p
        p = p * nums[i]
    
    p = 1
    for i in range(n-1,-1,-1):
        prods[i] = prods[i] * p
        p = p * nums[i]
    return prods

if __name__ == "__main__":
    nums = [1,2,3,4]
    res = productExceptSelfII(nums)
    print(res)