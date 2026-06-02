class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        res = []

        for k in range(len(nums)):
            if nums[k] > 0:
                return res
            
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i, j = k + 1, len(nums) - 1
            while i < j:
                if nums[k] + nums[i] + nums[j] == 0:
                    res.append([nums[k],nums[i],nums[j]])

                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[k] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    i += 1
        
        return res



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        
        return res



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        res = []

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















