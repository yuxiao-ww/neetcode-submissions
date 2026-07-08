class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        def backtracking(i):
            if i >= len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[i])
            backtracking(i + 1)
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i + 1)
        backtracking(0)
        return res