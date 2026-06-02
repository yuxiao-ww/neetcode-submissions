class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        
        # dict1
        count1 = {}
        for s in s1:
            count1[s] = 1 + count1.get(s, 0)
        print(count1)
        
        while r < len(s2) + 1:
            tmp = s2[l:r]
            tmp_count = {}
            for s in tmp:
                tmp_count[s] = 1 + tmp_count.get(s, 0)
            print(tmp_count)
            if count1 == tmp_count:
                return True
            l += 1
            r += 1
        
        return False

        