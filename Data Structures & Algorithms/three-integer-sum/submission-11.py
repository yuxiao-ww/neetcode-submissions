class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        res = []
        nums.sort()

        for k in range(len(nums)):
            if nums[k] > 0:
                return res
            
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i, j = k + 1, len(nums) - 1
            while i < j:
                if nums[k] + nums[i] + nums[j] == 0:
                    res.append([nums[k], nums[i], nums[j]])

                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    
                    i += 1
                    j -= 1

                elif nums[k] + nums[i] + nums[j] < 0:
                    i += 1
                else:
                    j -= 1
            
        return res