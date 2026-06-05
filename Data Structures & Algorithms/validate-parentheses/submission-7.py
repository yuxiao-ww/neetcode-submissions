class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        
        stack = []
        dic = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in dic:
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
