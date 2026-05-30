class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ['+', '-', '*', '/']
        for ch in tokens:
            if ch not in symbols:  # 不是运算符号是数字
                stack.append(ch)
            else:  # 是运算符号
                if stack:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    match ch:
                        case '+':
                            stack.append(num1 + num2)
                        case '-':
                            stack.append(num2 - num1)
                        case '*':
                            stack.append(num1 * num2)
                        case '/':
                            stack.append(int(num2 / num1))
        
        return int(stack[-1])

                