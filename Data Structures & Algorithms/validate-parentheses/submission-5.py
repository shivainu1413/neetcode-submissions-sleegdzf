class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'}': '{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c in char_map.values():
                stack.append(c)
            if c in char_map.keys():
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if char_map[c] != last:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False