'''
Max Profit:
    Write an efficient function that takes stock_prices and returns the best profit 
    I could have made from one purchase and one sale of one share of Apple stock yesterday.
    Input: [10, 7, 5, 8, 11, 9]
    Output: 6
'''
def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError('max profit need at least 2 prices')
        
    curr_min = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    
    for curr_price in stock_prices[1:]:
        pot_profit = curr_price - curr_min # get the potential profit
        max_profit = max(max_profit, pot_profit) # get the max profit
        curr_min = min(curr_min, curr_price) # update the current min

    return max_profit