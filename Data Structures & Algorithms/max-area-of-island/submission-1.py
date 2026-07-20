class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            area = 1

            while queue:
                row, col = queue.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(ROW) and 
                        c in range(COL) and 
                        grid[r][c] == 1 and
                        (r, c) not in visited
                    ):
                        queue.append((r, c))
                        visited.add((r, c))
                        area += 1
            return area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, bfs(r, c))
        
        return res
