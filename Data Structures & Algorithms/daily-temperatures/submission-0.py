class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调栈
        if len(temperatures) == 1:
            return [0]
        
        stack = [0]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        
        return result