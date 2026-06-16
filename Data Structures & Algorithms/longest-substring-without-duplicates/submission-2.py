class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sub_set = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in sub_set:
                sub_set.remove(s[left])
                left += 1
            sub_set.add(s[right])
            max_len = max(max_len, len(sub_set))
        return max_len