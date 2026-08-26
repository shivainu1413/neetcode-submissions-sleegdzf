class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            cost = 0
            for p in piles:
                cost += math.ceil(p / mid)
            if cost > h:
                left = mid + 1
            else:
                right = mid
        return left