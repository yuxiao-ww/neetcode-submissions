class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        # 1. 保存每个task的频率
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        # 2. 维护小顶堆，需要存负
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()

        # 3. or代表还有需要处理的task，可能在heap可能在queue
        while heap or queue:
            time += 1
            # 4. heap小顶堆代表要处理的task，按照频率高到低
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    queue.append([c, time + n])
            # 5. queue[0]代表还需要处理的次数（负），queue[1]代表轮到的时间
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()

        while heap or queue:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    queue.append([c, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time