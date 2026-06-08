# 前后缀
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        prefix, postfix = [0] * len(height), [0] * len(height)
        prefix[0] = height[0]
        postfix[-1] = height[-1]

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            postfix[i] = max(postfix[i + 1], height[i])

        for i in range(len(height)):
            res += min(prefix[i], postfix[i]) - height[i]

        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        prefix, postfix = [0] * len(height), [0] * len(height)

        prefix[0] = height[0]
        postfix[-1] = height[-1]

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            postfix[i] = max(postfix[i + 1], height[i])
        
        for i in range(len(height)):
            res += min(prefix[i], postfix[i]) - height[i]
        
        return res



class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, postfix = [0] * len(height), [0] * len(height)
        res = 0

        prefix[0] = height[0]
        postfix[-1] = height[-1]

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i])
        for i in range(len(height)-2, -1, -1):
            postfix[i] = max(postfix[i + 1], height[i])
        
        for i in range(len(height)):
            res += min(prefix[i], postfix[i]) - height[i]
        
        return res



class Solution:
    def trap(self, height: List[int]) -> int:
        pre, post = [0] * len(height), [0] * len(height)
        res = 0

        pre[0] = 1 * height[0]
        post[-1] = 1 * height[-1]

        for i in range(1, len(height)):
            pre[i] = max(pre[i - 1], height[i])
        for i in range(len(height)-2, -1, -1):
            post[i] = max(post[i + 1], height[i])
        
        for i in range(len(height)):
            res += min(pre[i], post[i]) - height[i]
        
        return res
















