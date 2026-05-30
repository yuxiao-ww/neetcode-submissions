class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):  # 从最后一位往前
            if digits[i] < 9:
                digits[i] += 1
                return digits  # 无需进位，直接返回
            digits[i] = 0  # 该位变 0，进位继续
        
        # 如果所有位都是 9，例如 [9,9,9] -> [1,0,0,0]
        return [1] + digits
