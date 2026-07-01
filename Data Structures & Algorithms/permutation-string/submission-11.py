class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count1, count2 = {}, {}
        for s in s1:
            count1[s] = 1 + count1.get(s, 0)
        for s in s2[:len(s1)]:
            count2[s] = 1 + count2.get(s, 0)
        
        i, j = 0, len(s1)
        while j < len(s2):
            print(i, j)
            if count1 == count2:
                return True
            # 右加
            count2[s2[j]] = 1 + count2.get(s2[j], 0)
            # 左减
            count2[s2[i]] -= 1
            if count2[s2[i]] == 0:
                del count2[s2[i]]
            i += 1
            j += 1

        return count1 == count2
