class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()

        i, j = 0, 1
        length = 1

        while j < len(nums):
            if nums[j] == nums[j - 1] + 1:
                length = max(length, j - i + 1)
            else:
                i = j
            j += 1
        
        return length