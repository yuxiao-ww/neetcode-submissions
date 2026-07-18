class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()

        while queue or heap:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    queue.append([c, time + n])
            
            if queue and queue[0][1] == time:
                task = queue.popleft()
                heapq.heappush(heap, task[0])
        
        return time
