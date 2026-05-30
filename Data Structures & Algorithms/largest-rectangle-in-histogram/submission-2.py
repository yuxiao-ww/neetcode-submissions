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