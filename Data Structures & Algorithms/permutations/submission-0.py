class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        path = []
        used = [False] * n

        def backtracking(path):
            print(path)
            if len(path) == n:
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtracking(path)
                    path.pop()
                    used[i] = False
        
        backtracking(path)
        return result
        