'''
Coin Change:
    Find the number of ways to make change for a certain amount
'''

def coin_change(amount, coins):
    
    combos = [0] * (amount + 1) # create an array of size amount + 1
    combos[0] = 1 # initialize the number of ways to get 0 coins (1 way)

    for coin in coins:
        for i in range(coin, amount + 1): # for every coin from [coin, amount + 1) 
            combos[i] += combos[i - coin] # add to the current spot the number of combos from combos[i - coin]
    return combos[amount]
