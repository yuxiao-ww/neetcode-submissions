class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        stack = stones
        while len(stack) > 1:
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append(abs(s1 - s2))
            stack.sort()
        return stack[0]

        