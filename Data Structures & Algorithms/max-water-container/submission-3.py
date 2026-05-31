class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                area = max(area, (j - i) * min(heights[i], heights[j]))
        return area


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            area = max(area, min(heights[r], heights[l]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area