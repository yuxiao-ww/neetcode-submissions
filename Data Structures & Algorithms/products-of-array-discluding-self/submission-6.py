class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        res = []

        prefix[0] = 1 * nums[0]
        postfix[-1] = 1 * nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                res.append(1 * postfix[1])
            elif i == len(nums) - 1:
                res.append(1 * prefix[i - 1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        
        return res
        