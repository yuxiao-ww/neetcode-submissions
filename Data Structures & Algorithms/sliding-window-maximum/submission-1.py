class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            max_value = max(nums[i: i+k])
            result.append(max_value)
        
        return result

