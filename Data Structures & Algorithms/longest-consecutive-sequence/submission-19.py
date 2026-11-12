class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        i, j = 0, 1
        cur = nums[0]
        res = 1
        tmp = 1
        while j < len(nums):
            if nums[j] == cur + 1:
                tmp += 1
                cur = nums[j]
                j += 1
            elif nums[j] == cur:
                j += 1
            else:
                cur = nums[j]
                tmp = 1
                j += 1
            res = max(res, tmp)
        return res





