class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = sorted_nums[i]
            left = i+1
            right = len(sorted_nums)-1
            while left < right:
                val = sorted_nums[left] + sorted_nums[right]
                if target == -val:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right+1]:
                        right -= 1
                elif target < -val:
                    left += 1
                else:
                    right -= 1
        return res
                