class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        from collections import Counter
        s1_map = Counter(s1)
        left = 0
        s2_map = Counter(s2[left:len(s1)])
        if s1_map == s2_map: return True
        for right in range(len(s1), len(s2)):
            s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1
            s2_map[s2[left]] -= 1
            if s2_map[s2[left]] <= 0:
                del s2_map[s2[left]]
            if s2_map == s1_map: return True
            left += 1
        return False
