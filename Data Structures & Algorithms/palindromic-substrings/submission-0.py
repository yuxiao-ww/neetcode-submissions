# dp[i][j]: i~j为结尾的子序列是否是回文序列
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        result += 1
                        dp[i][j] = True
        
        return result
            
        