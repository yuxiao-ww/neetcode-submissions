# 前后缀
class Solution:
    def trap(self, height: List[int]) -> int:
        pre, post = [0] * len(height), [0] * len(height)
        res = 0

        pre[0] = height[0]
        post[-1] = height[-1]

        for i in range(1, len(height)):
            pre[i] = max(pre[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            post[i] = max(post[i+1], height[i])
        
        for i in range(len(height)):
            res += min(pre[i], post[i]) - height[i]
        
        return res


# 双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxL, maxR = height[0], height[-1]
        l, r = 0, len(height) - 1

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        
        return res


# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        # find the first wall that greater than the current wall; both side
        # decreasing stack
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    w = i - stack[-1] - 1
                    h = min(left, right) - mid
                    res += h * w
            stack.append(i)
        
        return res














