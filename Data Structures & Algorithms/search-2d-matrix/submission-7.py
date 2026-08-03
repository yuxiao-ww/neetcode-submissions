class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        i, j = 0, ROW * COL - 1

        while i <= j:
            mid = (i + j) // 2
            r, c = mid // COL, mid % COL
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False