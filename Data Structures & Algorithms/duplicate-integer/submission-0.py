class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = []
        for num in nums:
            if num in tmp:
                return True
            tmp.append(num)
        
        return False
