class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        counts, countt = {}, {}
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        
        have, need = 0, len(countt)
        res, reslen = [-1, -1], float("inf")
        i = 0

        for j in range(len(s)):
            counts[s[j]] = 1 + counts.get(s[j], 0)

            if s[j] in countt and counts[s[j]] == countt[s[j]]:
                have += 1
            
            while have == need:
                size = j - i + 1
                if size < reslen:
                    res = [i, j]
                    reslen = min(reslen, size)
                
                counts[s[i]] -= 1
                if s[i] in countt and counts[s[i]] < countt[s[i]]:
                    have -= 1
                i += 1
        
        l, r = res
        return s[l: r + 1] if reslen != float("inf") else ""

            

