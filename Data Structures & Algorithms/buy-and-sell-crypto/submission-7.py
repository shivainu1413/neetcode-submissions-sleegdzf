class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow = 0
        max_profit = 0
        for fast in range(1, len(prices)):
            if prices[fast] < prices[slow]:
                slow = fast
            else:
                max_profit = max(max_profit, prices[fast] - prices[slow])
        return max_profit