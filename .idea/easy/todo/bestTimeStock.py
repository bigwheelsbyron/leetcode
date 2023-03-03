def maxProfit(prices):
    cheapestIndex = 0
    mostExpensiveIndex = 0
    currentProfit = prices[mostExpensiveIndex] - prices[cheapestIndex]
    for i in range(0,len(prices)):

        potentialProfit = prices[i] - prices[cheapestIndex]
        print(potentialProfit)
        #potential event 1:
            #i's profit is greater than current profit, make this the new best transaction
                #this would be because cheapest < most expensive < current Index
        if potentialProfit > currentProfit:
           mostExpensiveIndex = i
            #i's price is more than current cheapest, less than most expensive
                #cheapest < current Index < most expensive
                #ignore
            #i's price's is less than current cheapest
                ##two potential events from this, it may be more profitable to keep the current trade if the profit
                ##  made from the future trade using the cheapest value would be smaller than the profit made
                ##  using the more expensive purchase
                ##  it may however be better to proceed with the cheapest price


    return mostExpensiveIndex

print(maxProfit([7,1,5,3,6,4]))