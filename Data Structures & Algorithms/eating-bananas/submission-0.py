class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # 最小速度和最大速度

        while l < r:
            mid = (l + r) // 2
            
            # 计算珂珂在给定速度 mid 下吃完所有香蕉所需的总小时数
            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                r = mid
            else:
                l = mid + 1
        
        return l