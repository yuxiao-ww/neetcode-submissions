class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        sets = set()
        
        for r in range(len(s)):
            if s[r] not in sets:
                sets.add(s[r])
                longest = max(longest, r-l+1)
            else:
                while s[r] in sets:
                    sets.remove(s[l])
                    l += 1
                sets.add(s[r])
        
        return longest
