class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        def dfs(r, c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visited or
                grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            queue.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)
            dist += 1