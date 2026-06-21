class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for c in tokens:
            if c in operators:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if c == '+':
                    stack.append(n1 + n2)
                elif c == '-':
                    stack.append(n1 - n2)
                elif c == '*':
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))
            else:
                stack.append(int(c))
        return stack[-1]
