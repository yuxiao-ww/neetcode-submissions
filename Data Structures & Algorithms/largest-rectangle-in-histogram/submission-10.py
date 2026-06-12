class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        res = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                    right = i
                    w = right - left - 1
                    h = heights[mid]
                    res = max(res, h * w)
            else:
                stack.append(i)
        
        return res
        