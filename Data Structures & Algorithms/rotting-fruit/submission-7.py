class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        fresh = 0

        def rot(r, c):
            if (
                r in range(ROWS) and
                c in range(COLS) and
                grid[r][c] == 1 and
                (r, c) not in visit
            ):
                visit.add((r, c))
                queue.append([r, c])
                grid[r][c] = 2
                nonlocal fresh
                fresh -= 1

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
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            time += 1
        return time if not fresh else -1