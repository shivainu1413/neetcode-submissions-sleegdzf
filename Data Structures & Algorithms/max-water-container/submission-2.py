class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_area = 0
        while left < right:
            length = right - left
            short_bar = min(heights[left], heights[right])
            area = short_bar * length
            max_area = max(max_area, area)
            if short_bar == heights[left]:
                left += 1
            else:
                right -= 1
        return max_area
