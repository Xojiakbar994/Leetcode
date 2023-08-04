class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices: return 0
        else: 
            maxProfit = 0
            minPurchase = prices[0]

        for price in prices:
            curProfit = price - minPurchase
            if curProfit > maxProfit:
                    maxProfit = curProfit
            if price < minPurchase:
                    minPurchase = price
        return maxProfit
    
a = Solution()

print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([7,6,4,3,1]))