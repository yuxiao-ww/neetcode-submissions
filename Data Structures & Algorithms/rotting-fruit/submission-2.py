class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        fresh = 0
        queue = deque()

        def bfs(r, c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                grid[r][c] == 0
            ):
                return
            visit.add((r, c))
            queue.append((r, c))
            nonlocal fresh
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2 and (r, c) not in visit:
                    visit.add((r, c))
                    queue.append((r, c))
        
        time = 0
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            time += 1
        return time if not fresh else -1


