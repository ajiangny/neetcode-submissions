class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        curr_profit = 0

        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i and prices[j] > prices[i]:
                 curr_profit = prices[j] - prices[i]
                 if curr_profit > best_profit:
                    best_profit = curr_profit
        
        return best_profit