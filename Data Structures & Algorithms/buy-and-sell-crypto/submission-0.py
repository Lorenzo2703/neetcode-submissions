class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        difference=0

        for i in range(len(prices)):
            if prices[i]<price:
                price=prices[i]
            else:
                difference=max(difference,prices[i]-price)

        return difference