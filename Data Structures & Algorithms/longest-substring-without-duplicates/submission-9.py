class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        length = 1
        i, j = 0, 1
        while j < len(s):
            window = s[i:j]
            if s[j] not in window:
                j += 1
            else:
                i += 1
            length = max(length, j - i)
        
        return length

        