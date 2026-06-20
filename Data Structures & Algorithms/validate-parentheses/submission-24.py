class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []
        for c in s:
            if c not in valid:
                stack.append(c)
            else:
                if stack:
                    if stack[-1] != valid[c]:
                        return False
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False