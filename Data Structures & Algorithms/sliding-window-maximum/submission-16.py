class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        queue = deque([])
        res = []
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            if i - queue[0] >= k:
                queue.popleft()
            
            if i + 1 >= k:
                res.append(nums[queue[0]])
        
        return res


