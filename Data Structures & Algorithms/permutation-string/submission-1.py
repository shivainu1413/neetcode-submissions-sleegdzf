class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) > len(s2): return False
        left = 0
        s1_map = Counter(s1)
        for right in range(len(s1)-1, len(s2)):
            if s1_map == Counter(s2[left:right+1]):
                return True
            left += 1
        return False