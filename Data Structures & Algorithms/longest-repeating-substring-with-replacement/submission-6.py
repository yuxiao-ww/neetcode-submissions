class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        i, j = 0, 0
        count = {}
        res = 0

        for j in range(len(s)):
            count[s[j]] = 1 + count.get(s[j], 0)
            while (j - i + 1) - max(count.values()) > k: # valid
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res

