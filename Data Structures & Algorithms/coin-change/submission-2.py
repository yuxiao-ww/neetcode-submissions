# dp[j]: 凑足金额j所需要的最少金币个数
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0 and dp[i - coins[j]] != float('inf'):
                    dp[i] = min(dp[i - coins[j]] + 1, dp[i])
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]
        