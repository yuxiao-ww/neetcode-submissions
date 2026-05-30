class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new = []
        for l in matrix:
            new += l
        
        l, r = 0, len(new)-1
        while l <= r:
            mid = (l + r) // 2
            if new[mid] == target:
                return True
            elif new[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False