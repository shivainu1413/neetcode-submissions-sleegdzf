class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights)-1
        while left < right:
            length = right - left
            min_bar = min(heights[left], heights[right])
            max_area = max(max_area, min_bar * length)
            if min_bar == heights[left]:
                left += 1
            else:
                right -= 1
        return max_area
            
