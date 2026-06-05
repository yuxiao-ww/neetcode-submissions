class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        res = 1
        i, j = 0, 1
        while j < len(nums):
            if nums[j] == nums[j - 1] + 1:
                j += 1
            else:
                res = max(res, j - i)
                i = j
                j = i + 1
            res = max(res, j - i)
        return res



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i, j = 0, 1
        res = 1
        nums = list(set(nums))
        nums.sort()

        while j < len(nums):
            if nums[j] == nums[j - 1] + 1:
                res = max(res, j - i + 1)
            else:
                i = j
            j += 1
        
        return res




















