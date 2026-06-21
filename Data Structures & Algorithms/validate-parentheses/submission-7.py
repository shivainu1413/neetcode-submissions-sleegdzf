class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'}': '{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c in char_map:
                if len(stack) == 0:
                    return False
                if stack.pop() != char_map[c]:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False
                