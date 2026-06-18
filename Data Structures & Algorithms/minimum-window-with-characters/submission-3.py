class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        from collections import Counter
        need = Counter(t)
        need_count = len(need)
        have = 0
        res = ""
        res_len = float('inf')
        left = 0
        window = {}
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            while have == need_count:
                if (right - left + 1) < res_len:
                    res = s[left:right+1]
                    res_len = len(res)
                window[s[left]] -= 1
                if window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        return res
