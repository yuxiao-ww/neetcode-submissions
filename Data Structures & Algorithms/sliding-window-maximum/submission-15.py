class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        
        for i in range(len(nums)):
            # extend
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            # remove left
            if i - queue[0] + 1 > k:
                queue.popleft()
            
            # record
            if i >= k - 1:
                res.append(nums[queue[0]])
            
        return res
