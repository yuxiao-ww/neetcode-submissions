class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for row in matrix:
            array += row
        print(array)

        l, r = 0, len(array) - 1
        while l <= r:
            mid = (l + r) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                l += 1
            else:
                r -= 1
        return False