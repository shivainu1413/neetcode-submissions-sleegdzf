class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if len(s) < len(t): return ""
        need_map = Counter(t)
        need_count = len(need_map)
        left = 0
        have = 0
        window = {}
        res, res_len = "", float('inf')
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need_map and window[s[right]] == need_map[s[right]]:
                have += 1
            while have == need_count:
                if (right - left + 1) < res_len:
                    res = s[left:right+1]
                res_len = min(res_len, len(res))
                window[s[left]] -= 1
                if s[left] in need_map and window[s[left]] < need_map[s[left]]:
                    have -= 1
                left += 1
        return res
                    
