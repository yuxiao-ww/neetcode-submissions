class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            # add from right
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            # remove from left
            if l > queue[0]:
                queue.popleft()
            
            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1
            r += 1
        
        return res

