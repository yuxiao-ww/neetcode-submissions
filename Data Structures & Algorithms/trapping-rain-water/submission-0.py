class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        total_water = 0
        
        for i in range(n):
            left_max = max(height[:i+1])  # 找到 i 左侧最高的柱子
            right_max = max(height[i:])   # 找到 i 右侧最高的柱子
            total_water += min(left_max, right_max) - height[i]
        
        return total_water