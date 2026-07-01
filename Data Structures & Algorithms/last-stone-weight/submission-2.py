class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            s1 = stones.pop()
            s2 = stones.pop()
            stones.append(abs(s1 - s2))
            stones.sort()
        return stones[0]
