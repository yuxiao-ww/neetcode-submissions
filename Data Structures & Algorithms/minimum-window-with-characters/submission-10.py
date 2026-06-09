class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""
        
        countT, window = {}, {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in countT and window[ch] == countT[ch]:
                have += 1
            
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # shrink
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        counts, countt = {}, {}
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        
        have, need = 0, len(countt)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            counts[c] = 1 + counts.get(c, 0)

            if c in countt and counts[c] == countt[c]:
                have += 1
            
            while have == need:
                # record answer
                size = r - l + 1
                if size < resLen:
                    res = [l, r]
                    resLen = size
                
                # shrink
                counts[s[l]] -= 1
                if s[l] in countt and counts[s[l]] < countt[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""























