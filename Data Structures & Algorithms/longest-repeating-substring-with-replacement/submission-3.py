class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        l, r = 0, 0
        count = {}
        res = 0

        for r in range(len(s)):
            c = s[r]
            count[c] = 1 + count.get(c, 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
        
        return res
            
        