class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        i, j = 0, 0
        res = 0

        while j < len(prices):
            if prices[j] > prices[i]:
                res = max(res, prices[j] - prices[i])
            else:
                i = j
            j += 1
        
        return res