class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            count_map[s[right]] = count_map.get(s[right], 0) + 1
            max_char_len = max(count_map.values())
            while (right - left + 1) - max_char_len > k:
                count_map[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len