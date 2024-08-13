#modified Kadane's algo O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profitMax = 0
        profitCurr = 0

        for i in range(1, n):
            profitCurr += prices[i] - prices[i-1]
            if profitCurr > 0:
                pass
            else:
                profitCurr = 0

            profitMax = max(profitMax, profitCurr)
        
        return profitMax
