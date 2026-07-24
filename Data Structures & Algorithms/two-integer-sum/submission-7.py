class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if num not in map:
                map[target - num] = i
            else:
                return [map[num], i]