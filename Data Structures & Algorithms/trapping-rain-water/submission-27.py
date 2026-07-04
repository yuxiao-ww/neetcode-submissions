# 前后缀
class Solution:
    def trap(self, height: List[int]) -> int:
        pre, post = [0] * len(height), [0] * len(height)
        res = 0
        pre[0] = height[0]
        post[-1] = height[-1]

        for i in range(1, len(height)):
            pre[i] = max(pre[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            post[i] = max(post[i + 1], height[i])
        
        for i in range(len(height)):
            if i == 0:
                res += min(pre[0], post[0]) - height[0]
            if i == len(height) - 1:
                res += min(pre[-1], post[-1]) - height[-1]
            res += min(pre[i], post[i]) - height[i]
        
        return res


# 双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]
        res = 0
        while l <= r:
            if maxL < maxR:
                maxL = max(maxL, height[l])
                res += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                res += maxR - height[r]
                r -= 1
        return res


# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    w = i - stack[-1] - 1
                    h = min(left, right) - height[mid]
                    res += h * w
            stack.append(i)
        return res
                    

