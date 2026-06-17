class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 从右到左
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 从左到右
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                tmp = stack.pop()
                res[tmp] = i - tmp
            stack.append(i)
        return res
