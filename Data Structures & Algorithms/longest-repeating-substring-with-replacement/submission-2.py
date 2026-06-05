# 双指针
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        i, j = 0, 0
        length = 0
        count = {}

        while j < len(s):
            count[s[j]] = 1 + count.get(s[j], 0)
            
            while (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1
            
            length = max(length, j - i + 1)
            j += 1
        return length