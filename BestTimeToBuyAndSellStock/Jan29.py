# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.




class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        r = 1
        maxSoldProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxSoldProfit = max(diff, maxSoldProfit)
            else:
                l = r
                r += 1
            r += 1
        return maxSoldProfit

p = Solution()
print(p.maxProfit([4,5,5,5,32,3,2]))
        

        
