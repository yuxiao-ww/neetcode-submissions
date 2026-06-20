class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signals = "+-*/"
        stack = []

        for t in tokens:
            print(t)
            if t not in signals:
                stack.append(int(t))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == "+":
                    v = a + b
                elif t == "-":
                    v = b - a
                elif t == "*":
                    v = a * b
                elif t == "/":
                    v = b / a
                stack.append(int(v))
        return stack[0]
