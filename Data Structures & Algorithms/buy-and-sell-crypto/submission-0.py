class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        profit = 0

        for i in range(len(prices)):
            min_buy = min(min_buy, prices[i])
            profit = max(profit, prices[i] - min_buy)
        
        return profit