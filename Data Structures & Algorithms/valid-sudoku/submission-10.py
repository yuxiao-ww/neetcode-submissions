class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [[set() for _ in range(9)] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                if num in row[r] or num in col[c] or num in box[r//3][c//3]:
                    return False

                row[r].add(num)
                col[c].add(num)
                box[r//3][c//3].add(num)
        return True

                