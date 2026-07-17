class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        l, r = 0, 1
        result = 0
        while r < n:
            if prices[r] > prices[l]:
                result = max(prices[r]-prices[l], result)
            if prices[r] < prices[l]:
                l = r
            
            r+=1
            
        return result