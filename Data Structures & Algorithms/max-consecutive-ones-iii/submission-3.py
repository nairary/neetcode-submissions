class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        window = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                window+=1
            while window > k:
                result = max(result, r-l)
                window -= nums[l] == 0
                l+=1
        return max(result, r-l+1)
            
                