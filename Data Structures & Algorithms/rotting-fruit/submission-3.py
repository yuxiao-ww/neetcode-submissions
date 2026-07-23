class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        fresh = 0

        def bfs(r, c):
            if (
                r in range(ROWS) and
                c in range(COLS) and
                (r, c) not in visit and
                grid[r][c] == 1
            ):
                nonlocal fresh
                fresh -= 1
                queue.append([r, c])
                visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2 and (r, c) not in visit:
                    queue.append([r, c])
                    visit.add((r, c))
        
        time = 0
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            time += 1
        
        return time if not fresh else -1