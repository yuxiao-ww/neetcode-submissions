class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            dfs(i + 1, path, total + nums[i])
            path.pop()
            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path, total)
        dfs(0, path, 0)
        return res
