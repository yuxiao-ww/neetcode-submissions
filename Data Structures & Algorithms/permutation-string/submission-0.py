class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        l, r = 0, window_size
        count = defaultdict(int)
        # 统计 s1 频次
        for s in s1:
            count[s] += 1

        window = s2[l:r]
        count1 = defaultdict(int)
        # 统计 s2 初始窗口频次
        for s in window:
            count1[s] += 1
        
        # 先检查初始窗口是否匹配
        if count1 == count:
            return True

        # 滑动窗口
        while r < len(s2):

            count1[s2[l]] -= 1
            if count1[s2[l]] == 0:
                del count1[s2[l]] # 删除 0 值的键，确保字典比较时正确
            l += 1
            count1[s2[r]] += 1
            r += 1
        
            if count1 == count:
                return True
        
        return False