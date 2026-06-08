class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s2) < len(s1):
            return False
        count1, count2 = {}, {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        i, j = 0, len(s1)
        for c in s2[i:j]:
            count2[c] = 1 + count2.get(c, 0)
        
        while j < len(s2):
            if count2 == count1:
                return True
            
            c = s2[j]
            count2[c] = 1 + count2.get(c, 0)
            j += 1

            count2[s2[i]] -= 1
            if count2[s2[i]] == 0:
                del count2[s2[i]]
            i += 1
        
        return count1 == count2
