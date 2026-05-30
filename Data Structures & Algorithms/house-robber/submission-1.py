# dp[i]: 抢前i个房子，不包含i，的最大金额
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0] if n == 1 else 0
        
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = max(nums[1], nums[0])
        
        for i in range(2, n+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        
        return dp[-1]
