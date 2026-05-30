class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        start = 0
        nums.sort()

        def backtracking(path, start):
            result.append(path[:])
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(path, i+1)
                path.pop()
        
        backtracking(path, start)
        return result