class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]
        
        for i in range(len(nums)-1, 0, -1):
            if i == len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i + 1]
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = 1 * postfix[i + 1]
            elif i == len(nums) - 1:
                res[i] = prefix[i - 1] * 1
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        
        return res



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        res = []
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]
        
        for i in range(len(nums)-1, 0, -1):
            if i == len(nums)-1:
                postfix[len(nums)-1] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i + 1]
        
        for i in range(len(nums)):
            if i == 0:
                res.append(1 * postfix[i + 1])
            elif i == len(nums) - 1:
                res.append(1 * prefix[i - 1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        
        return res






















