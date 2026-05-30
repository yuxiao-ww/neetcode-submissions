class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        start = 0

        def backtracking(path, start):
            result.append(path[:])
            if start == len(nums):
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(path, i+1)
                path.pop()
        
        backtracking(path, start)
        return result

        