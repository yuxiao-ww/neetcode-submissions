class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [0] * len(nums), [0] * len(nums)
        res = [0] * len(nums)

        pre[0] = nums[0]
        post[-1] = nums[-1]

        # [1, 2, 8, 48]
        # [48, 48, 24, 6]
        # [48, 24, 12, 8]

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                res[0] = 1 * post[1]
            elif i == len(nums) - 1:
                res[-1] = 1 * pre[i - 1]
            else:
                res[i] = pre[i - 1] * post[i + 1]
        return res