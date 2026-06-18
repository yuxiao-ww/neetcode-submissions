class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
            r += 1
        
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i, j = 0, 1

        while j < len(prices):
            if prices[i] < prices[j]:
                res = max(res, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return res























