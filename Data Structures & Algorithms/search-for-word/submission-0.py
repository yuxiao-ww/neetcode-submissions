class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(i, j, k):
            # 如果当前字母匹配到最后一个，说明成功
            if k == len(word):
                return True
            # 越界 或 不匹配
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            # 选择：标记访问
            tmp = board[i][j]
            board[i][j] = "#"
            
            # 向四个方向探索
            res = (dfs(i+1, j, k+1) or
                   dfs(i-1, j, k+1) or
                   dfs(i, j+1, k+1) or
                   dfs(i, j-1, k+1))
            
            # 回溯：恢复现场
            board[i][j] = tmp
            return res
        
        # 从每个格子出发
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
