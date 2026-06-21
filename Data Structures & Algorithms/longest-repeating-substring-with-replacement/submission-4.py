class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        char_map = {}
        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            longest_char_len = max(char_map.values())
            while left < right and (right - left + 1) - longest_char_len > k:
                char_map[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len