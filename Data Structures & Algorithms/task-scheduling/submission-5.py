class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        
        heap = [-c for c in freq.values()]
        heapq.heapify(heap)
        queue = deque()

        time = 0
        while heap or queue:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c :
                    queue.append([c, time + n])
            if queue:
                if queue[0][1] == time:
                    task = queue.popleft()
                    heapq.heappush(heap, task[0])
        return time
