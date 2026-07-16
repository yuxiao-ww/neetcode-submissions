class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        def dfs(i, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(i + 1, path)
                    path.pop()
                    used[i] = False
        
        dfs(0, path)
        return res

