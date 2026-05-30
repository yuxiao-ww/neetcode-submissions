class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # 用哈希表存储所有数
        longest = 0  # 记录最长连续序列的长度

        for num in num_set:
            if num - 1 not in num_set:  # 只从序列起点开始找
                cur = num
                length = 1

                while cur + 1 in num_set:  # 向后扩展
                    cur += 1
                    length += 1
                
                longest = max(longest, length)
        
        return longest