class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            s1 = stones.pop()
            s2 = stones.pop()
            stones.append(s1 - s2)
            stones.sort()
        return stones[0]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            heapq.heappush(stones, -(abs(s1) - abs(s2)))
        return abs(stones[0])


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            heapq.heappush(stones, -(s1 - s2))
        return abs(stones[0])