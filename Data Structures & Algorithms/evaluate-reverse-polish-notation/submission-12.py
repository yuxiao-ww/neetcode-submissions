class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signals = "+-*/"

        for t in tokens:
            if t not in signals:
                stack.append(int(t))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+":
                    tmp = a + b
                elif t == "-":
                    tmp = a - b
                elif t == "*":
                    tmp = a * b
                else:
                    tmp = a / b
                stack.append(int(tmp))
        return stack[-1]
        