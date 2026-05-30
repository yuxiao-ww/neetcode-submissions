class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]  # 行检查
        col = [set() for _ in range(9)]  # 列检查
        box = [[set() for _ in range(3)] for _ in range(3)]  # 3x3 小方格检查

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                if num in row[i] or num in col[j] or num in box[i // 3][j // 3]:
                    return False
                
                row[i].add(num)
                col[j].add(num)
                box[i//3][j//3].add(num)
        
        return True

