class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue
                if c in row[i] or c in col[j] or c in box[i//3][j//3]:
                    return False
                
                row[i].add(c)
                col[j].add(c)
                box[i//3][j//3].add(c)
        return True