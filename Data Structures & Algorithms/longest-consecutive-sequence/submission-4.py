class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                temp = n
                count = 0
                while temp in nums_set:
                    count += 1
                    temp += 1
                max_len = max(count, max_len)
        return max_len