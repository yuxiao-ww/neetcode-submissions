class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [0] * len(nums), [0] * len(nums)
        res = []

        pre[0] = 1 * nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]
        
        post[-1] = 1 * nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                res.append(1 * post[1])
            elif i == len(nums) - 1:
                res.append(1 * pre[i - 1])
            else:
                res.append(pre[i - 1] * post[i + 1])
        
        return res
        