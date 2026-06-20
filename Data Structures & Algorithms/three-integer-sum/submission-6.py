class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = len(sorted_nums)-1
            while left < right:
                s = sorted_nums[left] + sorted_nums[right] + sorted_nums[i]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left-1] == sorted_nums[left]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right+1]:
                        right -= 1
        return res

            