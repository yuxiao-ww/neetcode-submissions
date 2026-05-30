class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        start = 0
        nums.sort()

        def backtracking(path, start, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                if total + nums[i] > target:
                    break
                
                path.append(nums[i])
                backtracking(path, i+1, total + nums[i])
                path.pop()
        
        backtracking(path, start, 0)
        return result
