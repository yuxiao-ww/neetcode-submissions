# dp[i]: 前i个子串能否被拆分
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)

        dp[0] = True  # 表示空字符串

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
        
        return dp[-1]

        