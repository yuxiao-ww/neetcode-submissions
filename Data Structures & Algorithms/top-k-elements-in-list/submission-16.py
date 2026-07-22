class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
