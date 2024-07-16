
# return number of combinations
def coinChangeII(coins, amount):
    memo = {} # (index, amoumt) -> number of combinations

    def f(i, amount):
        if (i, amount) in memo:
            return memo[(i,amount)]
        
        if i >= len(coins) or amount < 0:
            return 0
        
        if amount == 0 and i < len(coins):
            memo[(i,amount)] = 1
            return 1
        
        take = f(i, amount - coins[i])
        skip = f(i + 1, amount)
        
        memo[(i,amount)] = take + skip
        return take + skip

    return f (0, amount)

# return minimum amount of coins can used to achieved amount
def coinChange(coins, amount):
    if amount == 0: return 0
    res = amount + 1
    memo = {}
    
    def f(amountLeft, used): 
        nonlocal res
        if amountLeft < 0:
            # return -1
            return

        if amountLeft == 0:
            res = min(res, used)
            # return used

        for c in coins:
            if (amountLeft -c , used + 1) not in memo:
                f(amountLeft - c, used + 1)
                memo[(amountLeft - c, used + 1)] = True
    f(amount, 0)
    return res if res < amount + 1 else -1


def coinChangeDP(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1,len(dp)):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a - c] + 1, dp[a])
    
    return dp[-1] if dp[-1] < amount + 1 else -1


if __name__ == "__main__":
    res = coinChangeDP([1,5,10], 12)
    print(res)