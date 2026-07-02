class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        res = 1
        i, j = 0, 0
        seen = {}
        while j < len(s):
            print(s[i], s[j])
            if s[j] not in seen:
                seen[s[j]] = 1 + seen.get(s[j], 0)
                j += 1
                res = max(res, j - i)
            else:
                seen[s[i]] -= 1
                if seen[s[i]] == 0:
                    del seen[s[i]]
                i += 1
        return res


