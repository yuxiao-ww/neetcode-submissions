class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        counts, countt = {}, {}
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        
        i, j = 0, 0
        have, need = 0, len(countt)
        res, resLen = [-1, -1], float("inf")

        while j < len(s):
            c = s[j]
            counts[c] = 1 + counts.get(c, 0)
            # window = s[i:j]

            if c in countt and counts[c] == countt[c]:
                have += 1
            
            while have == need:
                size = j - i
                if size < resLen:
                    resLen = size
                    res = [i, j]
                
                counts[s[i]] -= 1
                if s[i] in countt and counts[s[i]] < countt[s[i]]:
                    have -= 1
                i += 1

            j += 1
        
        i, j = res
        return s[i:j+1] if resLen != float("inf") else ""
            


