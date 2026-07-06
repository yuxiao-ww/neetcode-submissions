class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i, path, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(path.copy())
                return
            
            # include nums[i]
            path.append(nums[i])
            backtrack(i, path, total + nums[i])

            # NOT include nums[i]
            path.pop()
            backtrack(i + 1, path, total)
        
        backtrack(0, path, 0)
        return res
