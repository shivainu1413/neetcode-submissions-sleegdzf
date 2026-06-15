class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        count = 0
        for i in range(1, len(left_max)):
            left_max[i] = max(height[i], left_max[i-1])
        for i in range(len(right_max)-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(n):
            min_bar = min(left_max[i], right_max[i])
            count += (min_bar - height[i])
        return count