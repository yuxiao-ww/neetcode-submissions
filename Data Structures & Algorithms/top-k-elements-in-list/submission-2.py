class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        min_heap = []
        for num, freq in dic.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 桶排序
        dic = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []

        for num, freq in dic.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
