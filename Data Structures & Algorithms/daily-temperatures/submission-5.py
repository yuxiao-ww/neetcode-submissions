class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # 单减
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            while stack and t >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
            
        return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                k = stack.pop()
                res[k] = i - k
            stack.append(i)
        
        return res
        
            
