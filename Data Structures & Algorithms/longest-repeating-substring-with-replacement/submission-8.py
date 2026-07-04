class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i, j = 0, 0
        res = 0
        while j < len(s):
            count[s[j]] = 1 + count.get(s[j], 0)
            j += 1
            window = s[i:j]
            if len(window) - max(count.values()) <= k:
                res = max(res, j - i)
            else:
                count[s[i]] -= 1
                i += 1
        return res
