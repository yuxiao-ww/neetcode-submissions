class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        n = len(s)
        # dp[i] = 前 i 个字符能不能被拆分(不包含i)
        dp = [False] * (n + 1)

        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j: i] in words:
                    dp[i] = True
                    break
        
        return dp[n]
