class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                return True
        return False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
