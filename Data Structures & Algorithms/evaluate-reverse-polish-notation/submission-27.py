class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        operators = "+-*/"
        stack = []
        res = 0
        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    tmp = a + b
                elif token == "-":
                    tmp = b - a
                elif token == "*":
                    tmp = a * b
                elif token == "/":
                    tmp = b / a
                stack.append(int(tmp))
            else:
                stack.append((int(token)))
        return stack[0]