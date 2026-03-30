class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for sub in s:
            if len(stack) == 0 and sub in [')', '}', ']']:
                return False
            if sub in ['(', '{', '[']:
                stack.append(sub)
            if sub in [')', '}', ']']:
                prev = stack.pop()
                if char_map[prev] != sub:
                    return False
        return True if len(stack) == 0 else False

