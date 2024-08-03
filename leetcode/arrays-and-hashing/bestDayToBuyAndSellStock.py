def maxProfit(prices):
    cheapestDay = prices[0]
    res = 0
    for price in prices[1:]:
        if price < cheapestDay:
            cheapestDay = price
        else:
            res = max(res, price - cheapestDay)

    return res


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4] # 5
    p = [7, 6, 4, 3, 1] # 0
    res = maxProfit(p)
    print(res)