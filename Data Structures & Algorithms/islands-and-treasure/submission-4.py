class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        def addRoom(r, c):
            if (
                r in range(ROWS) and
                c in range(COLS) and
                (r, c) not in visit and
                grid[r][c] != -1
            ):
                visit.add((r, c))
                queue.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r, c) not in visit:
                    visit.add((r, c))
                    queue.append([r, c])
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r, c + 1)
                addRoom(r - 1, c)
                addRoom(r, c - 1)
            dist += 1
        

