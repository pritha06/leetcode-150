'''
prices[i] is the price of a given stock on the ith day.
maximize your profit by choosing a single day to buy one stock and choosing a different day
in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
'''
'''
The trick : track the minimum price and the maximum possible profit
Keep track of the buy price --> keep comparing the current price with prvious buy price and
 track of the minimum price while iterating through the list
However, if the current price is greater than the previous buy price
now check if you sell it now would you get a better profit than the previous one
Keep track of the maximum profit

'''

def max_profit(prices):
    buy_price=prices[0]
    profit=0
    for i in range(1,len(prices)):
        if prices[i]<buy_price:
            buy_price=prices[i]
        else:
            profit=max(profit,prices[i]-buy_price)
    return profit

prices = [7,1,5,3,6,4]
result=max_profit(prices)
print(result)
