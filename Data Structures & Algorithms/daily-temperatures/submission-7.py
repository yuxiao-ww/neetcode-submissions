class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 从右到左
        res = [0] * len(temperatures)
        stack = []

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
        # 从左到右
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res