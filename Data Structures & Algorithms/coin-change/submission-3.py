class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 因为求最小，所以设最大
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0 # 凑出 0 元最少需要 0 枚硬币

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    # 看最后一枚硬币是什么
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return -1 if dp[amount] == float("inf") else dp[amount]