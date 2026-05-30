class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ["." * n for _ in range(n)]

        cols = set()
        diag1, diag2 = set(), set()

        def backtracking(row):
            if row == n:
                res.append(board[:])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtracking(row + 1)

                board[row] = board[row][:col] + '.' + board[row][col+1:]
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtracking(0)
        return res