class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target - nums[i]] = i
                print(dic)
            else:
                return [dic[nums[i]], i]
