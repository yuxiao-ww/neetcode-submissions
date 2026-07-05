class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        chars = "+-*/"
        stack = []
        for t in tokens:
            if t not in chars:
                stack.append(t)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == "+":
                    stack.append(a+b)
                if t == "-":
                    stack.append(b-a)
                if t == "*":
                    stack.append(a*b)
                if t == "/":
                    stack.append(b/a)
        return int(stack[0])