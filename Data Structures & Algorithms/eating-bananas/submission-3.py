class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = 0
        while left <= right:
            mid = (left+right)//2
            count = 0
            for p in piles:
                count += math.ceil(p/mid)
            if count > h:
                left = mid + 1
            else:
                right = mid - 1
                k = mid
        return k
