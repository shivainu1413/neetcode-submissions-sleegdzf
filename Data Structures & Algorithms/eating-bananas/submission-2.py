class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = 0
        min_count = float('inf')
        while left <= right:
            mid = (left+right)//2
            count = 0
            for p in piles:
                count += (p + (mid-1)) // mid
            if count <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        return k