class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for t in tokens:
            if t in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if t == '+':
                    stack.append(num1 + num2)
                if t == '-':
                    stack.append(num1 - num2)
                if t == '*':
                    stack.append(num1 * num2)
                if t == '/':
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(t))
        return stack[-1]