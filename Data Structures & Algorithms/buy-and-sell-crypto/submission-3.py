class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX_profit = 0
        l,r = 0,1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                MAX_profit = max(MAX_profit, profit)
            else:
                l = r
            r += 1

        return MAX_profit


