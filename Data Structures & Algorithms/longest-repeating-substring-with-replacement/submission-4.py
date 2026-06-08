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
            

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        count = {}
        i, j = 0, 0
        res = 1

        for j in range(len(s)):
            c = s[j]
            count[c] = 1 + count.get(c, 0)

            # if valid
            while (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1
            else:
                res = max(res, j - i + 1)
        
        return res






















