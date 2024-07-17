#  O(n) memory
def trapI(height):
    n = len(height)
    maxLeft = [0 for _ in range(n)]
    maxRight = [0 for _ in range(n)]
    canTrap = 0

    # calculate maxLeft
    cur = 0
    for i in range(n):
        maxLeft[i] = cur
        cur = max(cur, height[i])

    # calculate maxRight
    cur = 0
    for i in range(n - 1, -1, -1):
        maxRight[i] = cur
        cur = max(cur, height[i])

    # sum the final output:
    # for each i -> val = min(maxLeft , maxRight[i]) - height
    # כלומר בכל נקודה נוכל לשים מינימום גובה מקסימלי מצדדי שהוא לא אני פחות הגובה שלי
    # אם זה יוצא קטן מאפס אז זאת נקודת מינמום מקומי?

    for i in range(len(height)):
        val = min(maxLeft[i], maxRight[i]) - height[i]
        val = max(val, 0)
        canTrap += val

    return canTrap

def trapII(height):
    if not height: return 0

    canTrap = 0
    n = len(height)
    l = 0
    r  = n - 1
    maxLeft = height[l]
    maxRight = height[r]
    while l < r:
        if maxLeft <= maxRight:
            l += 1
            canTrap += max(maxLeft - height[l], 0) 
            maxLeft = max(maxLeft, height[l])
        else:
            r -= 1
            canTrap += max(maxRight - height[r], 0)
            maxRight = max(maxRight, height[r])
        
    return canTrap



if __name__ == "__main__":
    print("hello")
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = trapI(height)
    print(res)
    res = trapII(height)
    print(res)