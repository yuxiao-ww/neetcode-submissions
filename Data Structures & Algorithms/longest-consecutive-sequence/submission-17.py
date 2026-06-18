class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        res = 1
        i, j = 0, 1

        length = 1
        while j < len(nums):
            if nums[j] == nums[j - 1] + 1:
                length += 1
                j += 1
            elif nums[j] == nums[j - 1]:
                j += 1
            else:
                length = 1
                j += 1
            res = max(res, length)
        return res


