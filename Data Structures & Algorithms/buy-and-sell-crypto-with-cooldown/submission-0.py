class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1buy, dp2buy = 0, 0
        dp1sell = 0

        for i in range(n-1,-1,-1):
            buy = max(dp1sell-prices[i],dp1buy)
            sell = max(dp2buy+prices[i],dp1sell)

            dp2buy = dp1buy
            dp1buy,dp1sell = buy,sell

        return dp1buy