# 暴力
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            left = i
            right = i

            # 向左侧遍历：寻找第一个矮一级的柱子
            for _ in range(left, -1, -1):
                if heights[left] < heights[i]:
                    break
                left -= 1
            
            for _ in range(right, len(heights)):
                if heights[right] < heights[i]:
                    break
                right += 1
            
            w = right - left - 1
            h = heights[i]
            res = max(res, w * h)
        
        return res


# 暴力
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            min_h = float('inf')
            for j in range(i, n):
                min_h = min(min_h, heights[j])
                max_area = max(max_area, min_h * (j - i + 1))
        
        return max_area


# 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0

        for i in range(1, len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid = stack[-1]
                    stack.pop()
                    if stack:
                        left = stack[-1]
                        right = i
                        w = right - left - 1
                        h = heights[mid]
                        result = max(result, h * w)
                stack.append(i)
        
        return result


# 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        result = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
        
        return result