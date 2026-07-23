class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        result = 0
        l = 0
        for r in range(1, len(nums)):
            k-=(nums[r]-nums[r-1])*(r-l)
            while k < 0:
                k+=nums[r]-nums[l]
                l+=1
            result = max(result, r-l+1)
        return result