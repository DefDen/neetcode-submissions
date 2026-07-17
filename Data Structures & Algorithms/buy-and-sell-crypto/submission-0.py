class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        m = 0
        while r < len(prices):
            m = max(m, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return m