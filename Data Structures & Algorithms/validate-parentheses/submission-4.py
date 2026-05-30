class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for ch in s:
            if ch in dic.keys():
                stack.append(dic[ch])
            elif not stack or ch != stack[-1]:
                return False
            else:
                stack.pop()

        return True if not stack else False