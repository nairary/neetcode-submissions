class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp1 = [0] * (n-1)
        dp2 = [0] * (n-1)

        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        result = max(dp1[0], dp1[1])
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], nums[i]+dp1[i-2])
            result = max(result, dp1[i])
        
        nums = nums[1:]
        print(nums)
        dp2[0], dp2[1] = nums[0], max(nums[0], nums[1])
        result = max(result, dp2[0], dp2[1])
        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i-1], nums[i]+dp2[i-2])
            result = max(result, dp2[i])
            
        print(dp2)
        return result