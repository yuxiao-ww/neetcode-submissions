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





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        i, j = 0, 1
        length = 1
        while j < len(s):
            window = s[i:j]
            if s[j] not in window:
                length = max(length, j - i + 1)
                j += 1
            else:
                i += 1
        return length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l, r = 0, 1
        length = 1
        while r < len(s):
            window = s[l:r]
            if s[r] not in window:
                r += 1
                length = max(length, r - l)
            else:
                l += 1
        return length




















