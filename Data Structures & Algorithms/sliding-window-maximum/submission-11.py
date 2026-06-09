class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque()
        l, r = 0, 0

        for i, x in enumerate(nums):
            # queue insert from right
            while queue and x > nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            # queue remove from left
            if i - queue[0] + 1 > k:
                queue.popleft()

            # record answer
            if i >= k - 1:
                res.append(nums[queue[0]])
        
        return res



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        res = []
        queue = collections.deque()
        for i in range(len(nums)):
            # queue - in
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            
            # queue - out
            if i - queue[0] + 1 > k:
                queue.popleft()
            
            # record
            if i + 1 >= k:
                res.append(nums[queue[0]])
        
        return res























