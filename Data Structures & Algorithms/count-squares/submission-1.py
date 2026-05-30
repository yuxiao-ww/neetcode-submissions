class CountSquares:

    def __init__(self):
        self.Count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.Count[tuple(point)] += 1
        self.points.append(point)
        
    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.Count[(x, py)] * self.Count[(px, y)]
        return res
