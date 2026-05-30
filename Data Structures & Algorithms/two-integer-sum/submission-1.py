class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i, dic[target - nums[i]]] if i < dic[target - nums[i]] else [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i
        return 
