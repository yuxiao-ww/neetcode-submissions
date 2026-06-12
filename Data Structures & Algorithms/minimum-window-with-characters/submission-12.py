class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        counts, countt = {}, {}
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        
        have, need = 0, len(countt)
        res, reslen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            counts[c] = 1 + counts.get(c, 0)

            if c in countt and counts[c] == countt[c]:
                have += 1
            
            while have == need:
                size = r - l + 1
                if size < reslen:
                    reslen = size
                    res = [l, r]
                
                counts[s[l]] -= 1
                if s[l] in countt and counts[s[l]] < countt[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r + 1] if reslen != float("inf") else ""