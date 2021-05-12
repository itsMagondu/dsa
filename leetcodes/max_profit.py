def get_max_profit(prices):
    len_prices = len(prices)
    if len_prices < 2:
        return 0
    
    pointer = 1
    max_profit = 0

    while pointer < len_prices:
        if prices[pointer-1] < prices[pointer]:
          max_profit += (prices[pointer] - prices[pointer-1])
        
        pointer += 1

    return max_profit

prices = [7,1,2,3,4,5]
get_max_profit(prices)