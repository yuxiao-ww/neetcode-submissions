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



class Solution:
    def trap(self, height: List[int]) -> int:

        stack = [0]
        result = 0

        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    mid = height[stack[-1]]
                    stack.pop()
                    if stack:
                        rheight = height[i]
                        lheight = height[stack[-1]]

                        h = min(rheight, lheight) - mid
                        w = i - stack[-1] - 1
                        result += h * w
                stack.append(i)
        
        return result