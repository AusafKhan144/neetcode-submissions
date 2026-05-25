class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        buying_price = prices[0]
        max_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                buying_price = prices[right]
                left = right
                right += 1
            else:
                profit = prices[right] - buying_price
                max_profit = max(max_profit, profit)
                right += 1
        return max_profit

