class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        count = {}
        i, j = 0, 0
        res = 1
        while j < len(s):
            c = s[j]
            if c not in count:
                count[c] = 1 + count.get(c, 0)
                res = max(res, j - i + 1)
                j += 1
            else:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1
        return res

