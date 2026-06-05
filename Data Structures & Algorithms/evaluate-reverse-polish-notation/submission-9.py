class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signals = "+-*/"
        for t in tokens:
            if t not in signals:
                stack.append(t)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == "+":
                    tmp = a + b
                elif t == "-":
                    tmp = b - a
                elif t == '*':
                    tmp = a * b
                else:
                    tmp = b / a
                stack.append(tmp)
            print(stack)
        return int(stack[0])
