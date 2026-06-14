class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(type(sorted_nums))
        res = []
        for i in range(len(sorted_nums)):
            val = sorted_nums[i]
            left = i+1
            right = len(sorted_nums) - 1
            while left < right:
                temp = sorted_nums[left] + sorted_nums[right]
                if temp == - val:
                    if [sorted_nums[i], sorted_nums[left], sorted_nums[right]] not in res:
                        res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                elif temp < -val:
                    left += 1
                else:
                    right -= 1
        
        return res