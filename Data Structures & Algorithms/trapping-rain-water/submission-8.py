# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(left, right) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    r = height[i]
                    l = height[stack[-1]]
                    h = min(l, r) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res





















