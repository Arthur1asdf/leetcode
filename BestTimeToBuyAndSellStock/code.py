# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.




class Solution:
    def maxProfit(self, prices: List[int]) -> List[int]:
        maxProf = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > 0:
                    maxProf = max(diff, maxProf)
        return maxProf
p = Solution()
print(p.maxProfit([7, 1, 5, 3, 6, 4]))