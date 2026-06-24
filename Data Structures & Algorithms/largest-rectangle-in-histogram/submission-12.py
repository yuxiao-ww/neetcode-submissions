class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        heights.insert(0, 0)
        res = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                    right = i
                    h = heights[mid]
                    w = right - left - 1
                    res = max(res, h * w)
            
            stack.append(i)
        
        return res