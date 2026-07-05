class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for x, y in points:
            distances.append([x ** 2 + y ** 2, x, y])
        heapq.heapify(distances)

        while k - 1 >= 0:
            d, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1
        
        return res
        