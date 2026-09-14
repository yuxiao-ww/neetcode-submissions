class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[target - num] = i
            else:
                return [dic[num], i]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i , num in enumerate(nums):
            if num not in dic:
                dic[target - num] = i
            else:
                return [dic[num], i]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[target - num] = i
            else:
                return [dic[num], i]