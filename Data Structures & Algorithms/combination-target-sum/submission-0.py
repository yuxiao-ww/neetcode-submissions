class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        start = 0

        def backtracking(path, start, total):
            print(path)
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(path, i, total + nums[i])
                path.pop()
        
        backtracking(path, start, 0)
        return result
