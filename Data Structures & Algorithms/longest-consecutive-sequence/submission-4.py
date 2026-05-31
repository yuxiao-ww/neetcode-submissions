class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()
        i, j = 0, 1
        res = 0
        length = 1

        while i < len(nums) and j < len(nums):
            if nums[j] == nums[j-1] + 1:
                length += 1
                j += 1
            else:
                res = max(length, res)
                i = j
                j = i + 1
                length = 1
        res = max(length, res)
        return res
