# dp[i][0]: 第i天持有股票
# dp[i][1]: 第i天保持卖出股票
# dp[i][2]: 第i天卖出
# dp[i][3]: 第i天冷冻期
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]

        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], max(dp[i-1][3], dp[i-1][1]) - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        
        return max(dp[-1][1], dp[-1][2], dp[-1][3])
        