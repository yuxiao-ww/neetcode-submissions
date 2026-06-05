# brute force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit


# 双指针
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        return profit