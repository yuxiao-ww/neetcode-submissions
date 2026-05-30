# dp[i][j]: 用下标为[0,i]的nums能够凑满容量为j的背包，有多少种方法
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 分成+-两组
        total = sum(nums)
        if abs(target) > total:
            return 0
        if (target + total) % 2 == 1:
            return 0
        
        bagSize = (target + total) // 2

        dp = [[0] * (bagSize + 1) for _ in range(len(nums) + 1)]

        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(bagSize + 1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]

        