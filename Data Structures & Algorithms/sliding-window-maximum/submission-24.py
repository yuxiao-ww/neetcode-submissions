class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []

        for i, num in enumerate(nums):
            # right in
            while queue and num > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            
            # left out
            if i - queue[0] >= k:
                queue.popleft()

            # record max
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res
