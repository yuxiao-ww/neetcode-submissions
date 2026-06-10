class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()

        for i in range(len(nums)):
            print(queue)
            # append
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            # popleft
            if i - queue[0] + 1 > k:
                queue.popleft()
            
            # record
            if i + 1 >= k:
                res.append(nums[queue[0]])
        
        return res
