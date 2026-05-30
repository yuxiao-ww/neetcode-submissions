class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while 1:
            sums = 0
            n = str(n)
            for i in n:
                sums += int(i) ** 2
            
            if sums in visit:
                return False
            elif sums == 1:
                return True
            else:
                visit.add(sums)
            n = sums
        
        return False
        