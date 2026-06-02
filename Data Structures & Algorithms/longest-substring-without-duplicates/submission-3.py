class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l, r = 0, 1
        length = 1

        while r < len(s):
            window = s[l:r]
            if s[r] not in window:
                length = max(length, r - l + 1)
                r += 1
            else:
                l += 1
        
        return length

        