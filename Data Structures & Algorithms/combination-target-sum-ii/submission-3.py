class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def backtrack(i, path, total):
            if total == target:
                res.append(path.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            # include
            path.append(nums[i])
            backtrack(i + 1, path, total + nums[i])
            
            # not include
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, path, total)
        
        backtrack(0, path, 0)
        return res

