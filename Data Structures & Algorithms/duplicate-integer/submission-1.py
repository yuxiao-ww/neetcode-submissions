class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = []
        for num in nums:
            if num in tmp:
                return True
            tmp.append(num)
        
        return False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False