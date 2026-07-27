class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        res = []
        for k in range(len(nums)):
            # if nums[k] > 0:
            #     break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                else:
                    j -= 1
        
        return res