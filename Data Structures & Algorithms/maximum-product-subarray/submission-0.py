class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxdp = nums[0]
        mindp = nums[0]
        res = nums[0]

        for num in nums[1:]:
            a = num
            b = num * maxdp
            c = num * mindp

            maxdp = max(a, b, c)
            mindp = min(a, b, c)

            res = max(res, maxdp)
        
        return res