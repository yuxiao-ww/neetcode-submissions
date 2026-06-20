class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)