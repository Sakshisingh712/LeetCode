class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        minPrice = prices[0]
        for i in range(1, n):
            maxProfit = max(maxProfit, (prices[i] - minPrice))
            minPrice = min(minPrice, prices[i])
        return maxProfit


