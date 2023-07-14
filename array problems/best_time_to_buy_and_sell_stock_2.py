'''
Que-On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
'''
'''
approach- You can do it on a day-to-day basis. If buying on day 1 and selling on day 2 is profitable, do it. If buying on day 2 and selling on day 3 is profitable, do it. And so on. Yes, you can do both day1-to-day2 and day2-to-day3, even though there are multiple transactions on day 2. Either think of it as selling first and then buying later on that day, or think of it as keeping instead of selling+buying.
'''
'''
Greedy value concept, can also be solved later by dp
summations of price gain:
Time Complexity: O(n), for single level for loop
Space Complexity: O(n), for array storage sapce
code- 
price_gain = []
        
for idx in range( len(prices)-1 ):
    
    if prices[idx] < prices[idx+1]:
        
        price_gain.append( prices[idx+1]- prices[idx])
        
return sum( price_gain )
'''

'''approach2
Time Complexity: O(n), for single level for loop
Space Complexity: O(1), for fixed size of temporary variables
code-
'''

def max_profit(prices):
    max_profit=0
    
    for i in range(len(prices)-1):
        if prices[i]<prices[i+1]:
            max_profit+=prices[i+1]-prices[i]
    return max_profit

'''
Python's zip is also quite nice, and you can give it lists of different sizes, 
which none of the similar solutions I've seen from others exploited.
we find all peaks and related bottom elements, then sum all peaks minus all bottoms.
def maxProfit(self, prices):
    return sum(b-a for a,b in zip(prices,prices[1:])if b>a)
'''        

'''
approach 4:is to find all the local minima and maxima in the given array of prices.
 We buy the stock at the local minima and sell it at the corresponding local maxima. 
By doing this, we can accumulate the maximum profit.
Approach:
Initialize the variables profit and minPrice to 0 and INT_MAX respectively.
Iterate through the prices array using a for loop.
For each price at index i:
a. Update the minPrice by taking the minimum of the current minPrice and prices[i].
b. If the difference between prices[i] and minPrice is greater than 0, it means there is a profit to be made.
Add this profit to the profit variable.
Update the minPrice to prices[i] since we have sold the stock at this price.
Return the profit.
code-
profit=0
min_price=float('inf')
for i in range(len(prices)):
    min_price=min(min_price,prices[i])
    if prices[i]-min_price>0:
        profit+=prices[i]-min_price
        min_price=prices[i]
return profit

'''
prices = [7,1,5,3,6,4]
result=max_profit(prices)
print(result)