class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 0, 0

        for j in range(len(prices)):
            buy = prices[j]
            for i in range(j + 1, len(prices)):
                sell = prices[i]
                difference = sell - buy
                profit = max(profit, difference)
        
        return profit
            


