class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuyPrice = prices[0]
        profit = 0

        for price in prices:
            if price < bestBuyPrice:
                bestBuyPrice = price
            
            temp = price - bestBuyPrice
            if temp > profit:
                profit = temp

        return profit



