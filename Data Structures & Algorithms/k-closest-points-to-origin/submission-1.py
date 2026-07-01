class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distances = []
        for x, y in points:
            distances.append([x ** 2 + y ** 2, x, y])
        heapq.heapify(distances)

        while len(res) < k:
            d, x, y = heapq.heappop(distances)
            res.append([x, y])
        return res

