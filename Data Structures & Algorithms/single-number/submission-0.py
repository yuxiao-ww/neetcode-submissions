class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        first, second = [], []
        for num in nums:
            if num not in first:
                first.append(num)
            else:
                second.append(num)
        return sum(first) - sum(second)

        