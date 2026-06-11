class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        res = 0
        i, j = 0, 0
        count = {}

        for j in range(len(s)):
            c = s[j]
            count[c] = 1 + count.get(c, 0)

            while (j - i + 1) - max(count.values()) > k: # invalid
                # shrink
                count[s[i]] -= 1
                i += 1
            else:
                res = max(res, j - i + 1)
        
        return res
                
                
            

