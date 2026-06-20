# 前后缀
class Solution:
    def trap(self, height: List[int]) -> int:
        pre, post = [0] * len(height), [0] * len(height)
        pre[0] = height[0]
        post[-1] = height[-1]
        res = 0

        for i in range(1, len(height)):
            pre[i] = max(pre[i - 1], height[i])
        for i in range(len(height)-2, -1, -1):
            post[i] = max(post[i + 1], height[i])
        
        for i in range(len(height)):
            res += min(pre[i], post[i]) - height[i]
        return res


# 双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                res += maxR - height[r]
        return res









