class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for left in range(len(prices)):
            for right in range(left+1, len(prices)):
                max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit
