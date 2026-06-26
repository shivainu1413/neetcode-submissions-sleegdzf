class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            k = (right + left) // 2
            hours = sum((pile + k - 1) // k for pile in piles)
            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res