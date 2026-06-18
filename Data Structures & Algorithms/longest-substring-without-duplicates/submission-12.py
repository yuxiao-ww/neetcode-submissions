class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        res = 1
        i, j = 0, 1

        while j < len(s):
            if s[j] not in s[i:j]:
                j += 1
                res = max(res, j - i)
            else:
                i += 1
            
        return res