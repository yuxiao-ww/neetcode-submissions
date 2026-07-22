class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def bfs(r, c):
            area = 1
            queue = deque()
            visit.add((r, c))
            queue.append([r, c])

            while queue:
                row, col = queue.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1 and
                        (r, c) not in visit
                    ):
                        visit.add((r, c))
                        area += 1
                        queue.append([r, c])
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea