class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visit = set()

        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append([r, c])
            area = 1

            while queue:
                row, col = queue.popleft()
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visit and
                        grid[r][c] == 1
                    ):
                        visit.add((r, c))
                        queue.append([r, c])
                        area += 1
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, bfs(r, c))
        return res