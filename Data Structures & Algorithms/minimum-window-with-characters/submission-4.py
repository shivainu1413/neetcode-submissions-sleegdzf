class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        from collections import Counter
        need_map = Counter(t)
        need_count = len(need_map)
        window = {}
        have = 0
        res, res_len = "", float('inf')
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need_map and window[s[right]] == need_map[s[right]]:
                have += 1
            while have == need_count:
                if res_len > (right - left + 1):
                    res = s[left:right+1]
                    res_len = min(res_len, right-left+1)
                window[s[left]] -= 1
                if window[s[left]] < need_map[s[left]]:
                    have -= 1
                left +=1
        return res
        