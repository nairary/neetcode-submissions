class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        l, r = 0, 1
        profit = 0
        while l < n:
            while r < n and prices[r] < prices[l]:
                l +=1
                r +=1
            while r < n and prices[r] >= prices[l]:
                local_profit = prices[r]-prices[l]
                if local_profit > profit:
                    profit = local_profit
                r+=1
            l = r
            r = l+1
        
        return profit