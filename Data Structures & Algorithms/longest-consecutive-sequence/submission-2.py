class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        for n in nums:
            count = 0
            temp = n
            if n-1 not in nums_set:
                while temp in nums_set:
                    count += 1
                    temp += 1
                max_len = max(max_len, count)
        return max_len