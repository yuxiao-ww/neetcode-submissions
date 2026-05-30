# dp[i]: 以nums[i]为结尾的子串的和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        res = dp[0]

        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            if dp[i] > res:
                res = dp[i]
        
        return res
        
        