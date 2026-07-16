class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append([x ** 2 + y ** 2, x, y])
        heapq.heapify(distances)

        res = []
        while k:
            _, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1
        
        return res

