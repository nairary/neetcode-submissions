class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        profit = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                profit+=customers[i]
        result = profit
        result_l = 0

        l = 0
        for r in range(minutes, len(grumpy)):
            if grumpy[r] == 1:
                profit+=customers[r]
            if grumpy[l] == 1:
                profit-=customers[l]
            l+=1
            if profit > result:
                result = profit
                result_l = l
        
        for i in range(minutes):
            grumpy[result_l+i] = 0
        
        final_result = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                final_result+=customers[i]
        
        return final_result